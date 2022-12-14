terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "4.33.0"
    }
    tls = {
      source = "hashicorp/tls"
      version = "4.0.3"
    }
  }
}


provider "google" {}

provider "tls" {}


