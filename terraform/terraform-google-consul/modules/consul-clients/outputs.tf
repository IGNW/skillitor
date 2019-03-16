output "gcp_region" {
  value = "${var.gcp_region}"
}

output "cluster_name" {
  value = "${var.cluster_name}"
}

output "cluster_tag_name" {
  value = "${var.cluster_tag_name}"
}

output "instance_group_url" {
  value = "${google_compute_region_instance_group_manager.consul_clients.self_link}"
}

output "instance_group_name" {
  value = "${google_compute_region_instance_group_manager.consul_clients.name}"
}

output "instance_template_url" {
  value = "${data.template_file.compute_instance_template_self_link.rendered}"
}

output "instance_template_name" {
  value = "${element(concat(google_compute_instance_template.consul_clients_public.*.name, google_compute_instance_template.consul_clients_private.*.name), 0)}"
}

output "instance_template_metadata_fingerprint" {
  value = "${element(concat(google_compute_instance_template.consul_clients_public.*.metadata_fingerprint, google_compute_instance_template.consul_clients_private.*.metadata_fingerprint), 0)}"
}

output "firewall_rule_intracluster_url" {
  value = "${google_compute_firewall.allow_intracluster_consul.self_link}"
}

output "firewall_rule_intracluster_name" {
  value = "${google_compute_firewall.allow_intracluster_consul.name}"
}

output "firewall_rule_inbound_http_url" {
  value = "${element(concat(google_compute_firewall.allow_inbound_http_api.*.self_link, list("")), 0)}"
}

output "firewall_rule_inbound_http_name" {
  value = "${element(concat(google_compute_firewall.allow_inbound_http_api.*.name, list("")), 0)}"
}

output "firewall_rule_inbound_dns_url" {
  value = "${element(concat(google_compute_firewall.allow_inbound_dns.*.self_link, list("")), 0)}"
}

output "firewall_rule_inbound_dns_name" {
  value = "${element(concat(google_compute_firewall.allow_inbound_dns.*.name, list("")), 0)}"
}
