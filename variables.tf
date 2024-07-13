ariable "aws_region" {
  description = "The AWS region to deploy in"
  default     = "us-east-1"
}

variable "instance_type" {
  description = "The EC2 instance type"
  default     = "t2.micro"
}

variable "ami" {
  description = "The AMI ID"
  default     = "ami-0c55b159cbfafe1f0" # Replace with a suitable AMI for your needs
}

variable "key_name" {
  description = "The name of the SSH key pair"
  default     = "your_key_pair_name" # Replace with your actual key pair name
}
