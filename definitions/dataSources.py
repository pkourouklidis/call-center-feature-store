from feast import FileSource

callLogs = FileSource(
    name="callcenterSource",
    path="s3://feast/data/train.parquet",
    s3_endpoint_override="http://minio-service.kubeflow.svc.cluster.local:9000",  # Needed since s3fs defaults to us-east-1
    timestamp_field="ts",
    description="callcenter logs",
)