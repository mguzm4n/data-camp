variable "project" {
  description = "Project"
  default     = "sublime-seat-484418-h6"
}

variable "region" {
  description = "Region"
  default     = "use-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}



variable "gcs_bucket_name" {
  description = "Bucket Storage Name"
  default     = "sublime-seat-484418-h6-demo-bucket-this-must-be-unique"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
