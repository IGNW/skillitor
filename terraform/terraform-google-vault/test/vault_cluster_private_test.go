package test

import (
	"fmt"
	"strings"
	"testing"
	"time"

	"github.com/gruntwork-io/terratest/modules/gcp"
	"github.com/gruntwork-io/terratest/modules/logger"
	"github.com/gruntwork-io/terratest/modules/random"
	"github.com/gruntwork-io/terratest/modules/retry"
	"github.com/gruntwork-io/terratest/modules/ssh"
	"github.com/gruntwork-io/terratest/modules/terraform"
	"github.com/gruntwork-io/terratest/modules/test-structure"
)

const TFVAR_NAME_BASTION_SERVER_NAME = "bastion_server_name"

func runVaultPrivateClusterTest(t *testing.T, osName string) {
	exampleDir := test_structure.CopyTerraformFolderToTemp(t, "../", "examples/vault-cluster-private")

	defer test_structure.RunTestStage(t, "teardown", func() {
		terraformOptions := test_structure.LoadTerraformOptions(t, exampleDir)
		terraform.Destroy(t, terraformOptions)
	})

	defer test_structure.RunTestStage(t, "log", func() {
		//ToDo: Modify log retrieval to go through bastion host
		//      Requires adding feature to terratest
		//writeVaultLogs(t, "vaultPublicCluster", exampleDir)
	})

	test_structure.RunTestStage(t, "deploy", func() {
		projectId := test_structure.LoadString(t, WORK_DIR, SAVED_GCP_PROJECT_ID)
		region := test_structure.LoadString(t, WORK_DIR, SAVED_GCP_REGION_NAME)
		imageID := test_structure.LoadArtifactID(t, WORK_DIR)

		// GCP only supports lowercase names for some resources
		uniqueID := strings.ToLower(random.UniqueId())

		consulClusterName := fmt.Sprintf("consul-test-%s", uniqueID)
		vaultClusterName := fmt.Sprintf("vault-test-%s", uniqueID)

		terraformOptions := &terraform.Options{
			TerraformDir: exampleDir,
			Vars: map[string]interface{}{
				TFVAR_NAME_GCP_PROJECT_ID:                     projectId,
				TFVAR_NAME_GCP_REGION:                         region,
				TFVAR_NAME_CONSUL_SERVER_CLUSTER_NAME:         consulClusterName,
				TFVAR_NAME_CONSUL_SOURCE_IMAGE:                imageID,
				TFVAR_NAME_CONSUL_SERVER_CLUSTER_MACHINE_TYPE: "g1-small",
				TFVAR_NAME_VAULT_CLUSTER_NAME:                 vaultClusterName,
				TFVAR_NAME_VAULT_SOURCE_IMAGE:                 imageID,
				TFVAR_NAME_VAULT_CLUSTER_MACHINE_TYPE:         "g1-small",
				TFVAR_NAME_BASTION_SERVER_NAME:                fmt.Sprintf("bastion-test-%s", uniqueID),
			},
		}

		test_structure.SaveTerraformOptions(t, exampleDir, terraformOptions)

		terraform.InitAndApply(t, terraformOptions)
	})

	test_structure.RunTestStage(t, "validate", func() {
		terraformOptions := test_structure.LoadTerraformOptions(t, exampleDir)
		projectId := test_structure.LoadString(t, WORK_DIR, SAVED_GCP_PROJECT_ID)
		region := test_structure.LoadString(t, WORK_DIR, SAVED_GCP_REGION_NAME)
		instanceGroupId := terraform.OutputRequired(t, terraformOptions, TFOUT_INSTANCE_GROUP_ID)

		sshUserName := "terratest"
		keyPair := ssh.GenerateRSAKeyPair(t, 2048)
		saveKeyPair(t, exampleDir, keyPair)
		addKeyPairToInstancesInGroup(t, projectId, region, instanceGroupId, keyPair, sshUserName)

		bastionName := terraform.OutputRequired(t, terraformOptions, TFVAR_NAME_BASTION_SERVER_NAME)
		bastionInstance := gcp.FetchInstance(t, projectId, bastionName)
		bastionInstance.AddSshKey(t, sshUserName, keyPair.PublicKey)
		bastionHost := ssh.Host{
			Hostname:    bastionInstance.GetPublicIp(t),
			SshUserName: sshUserName,
			SshKeyPair:  keyPair,
		}

		cluster := initializeAndUnsealVaultCluster(t, projectId, region, instanceGroupId, sshUserName, keyPair, &bastionHost)
		testVaultUsesConsulForDns(t, cluster, &bastionHost)
	})
}

// SSH to a Vault node and make sure that is properly configured to use Consul for DNS so that the vault.service.consul
// domain name works.
func testVaultUsesConsulForDns(t *testing.T, cluster *VaultCluster, bastionHost *ssh.Host) {
	// Pick any host, it shouldn't matter
	host := cluster.Standby1

	command := "vault status -address=https://vault.service.consul:8200"
	description := fmt.Sprintf("Checking that the Vault server at %s is properly configured to use Consul for DNS: %s", host.Hostname, command)
	logger.Logf(t, description)

	maxRetries := 10
	sleepBetweenRetries := 5 * time.Second

	_, err := retry.DoWithRetryE(t, description, maxRetries, sleepBetweenRetries, func() (string, error) {
		o, e := runCommand(t, bastionHost, &host, command)
		logger.Logf(t, "Output from command vault status call to vault.service.consul: %s", o)
		return o, e
	})

	if err != nil {
		t.Fatalf("Failed to run vault command with vault.service.consul URL due to error: %v", err)
	}
}
