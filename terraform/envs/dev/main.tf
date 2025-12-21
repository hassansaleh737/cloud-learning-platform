provider "aws" {
  region = "us-east-1"
}

module "vpc" {
  source = "../../modules/vpc"
  cidr   = "10.0.0.0/16"
  env    = "dev"
}
provider "aws" {
  region = "us-east-1"
}

module "vpc" {
  source = "../../modules/vpc"
  cidr   = "10.0.0.0/16"
  env    = "dev"
}

module "chat_s3" {
  source  = "../../modules/s3"
  env     = "dev"
  service = "chat-service"
}
