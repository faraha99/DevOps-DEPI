provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "depi_instance" {
  ami           = var.ami
  instance_type = var.instance_type
  key_name      = var.key_name

  provisioner "local-exec" {
    command = "ansible-playbook -i ${self.public_ip}, -u ec2-user --private-key /path/to/your/private/key deploy.yml"
  }

  tags = {
    Name = "depi-instance"
  }
}

output "instance_ip" {
  value = aws_instance.depi_instance.public_ip
}
