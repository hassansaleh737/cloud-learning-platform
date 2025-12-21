provider "aws" {
  region = "us-east-1"
}

module "vpc" {
  source = "../../modules/vpc"
  cidr   = "10.1.0.0/16"
  env    = "staging"
}
