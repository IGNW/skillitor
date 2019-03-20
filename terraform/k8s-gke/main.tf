provider "google" {
  credentials = "${file("./creds/serviceaccount.json")}"
  project     = var.gcp_project_id
  region      = var.gcp_region
}

resource "google_container_cluster" "gke-cluster" {
  name               = "skillitor"
  network            = "default"
  zone               = var.gcp_zone
  initial_node_count = 3
}
#
#resource "google_container_node_pool" "node-pool" {
#  name               = "skillitor-node-pool"
#  zone               = var.gcp_zone
#  cluster            = "${google_container_cluster.gke-cluster.name}"
#  initial_node_count = 3
#}
