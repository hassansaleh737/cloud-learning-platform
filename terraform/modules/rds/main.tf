resource "aws_db_instance" "this" {
  identifier = "${var.env}-${var.service}-db"
  engine     = "postgres"
  engine_version = "17.6"
  instance_class = "db.t3.medium"

  storage_encrypted = true
  publicly_accessible = false
  skip_final_snapshot = true

  tags = {
    Name = "${var.env}-${var.service}-db"
  }
}
