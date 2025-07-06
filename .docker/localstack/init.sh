#!/usr/bin/env bash
# This script is used to initialize the localstack container with necessary configurations.

echo "Initializing LocalStack..."

echo "Creating S3 bucket..."
awslocal s3 mb s3://client-reports

echo "Setup Finished."