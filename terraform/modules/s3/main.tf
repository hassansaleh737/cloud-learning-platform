resource "aws_kms_key" "this" {
  description = "${var.env}-${var.service}-kms-key"
  enable_key_rotation = true
}

resource "aws_s3_bucket" "this" {
  bucket = "${var.service}-storage-${var.env}-project"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "this" {
  bucket = aws_s3_bucket.this.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = aws_kms_key.this.arn
    }
  }
}
