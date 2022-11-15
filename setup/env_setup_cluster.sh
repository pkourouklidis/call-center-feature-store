#!/bin/bash
export FEAST_S3_ENDPOINT_URL="http://minio-service.kubeflow.svc.cluster.local:9000"
export AWS_ACCESS_KEY_ID="minio"
export AWS_SECRET_ACCESS_KEY="minio123"
export FEAST_USAGE=False