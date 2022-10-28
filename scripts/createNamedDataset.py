from feast import FeatureStore
from feast.infra.offline_stores.file_source import SavedDatasetFileStorage
from feast.infra.offline_stores.contrib.postgres_offline_store.postgres_source import SavedDatasetPostgreSQLStorage
import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#setup the credentials needed to access the minio bucket
os.environ["AWS_SECRET_ACCESS_KEY"] = "minio123"
os.environ["AWS_ACCESS_KEY_ID"] = "minio"
os.environ["FEAST_S3_ENDPOINT_URL"] = "http://minio-service.kubeflow.svc.cluster.local:9000"

store = FeatureStore(repo_path="../definitions")

# Get the latest feature values for unique entities
historicalJob = store.get_historical_features(
    entity_df="select id, arrival_time as event_timestamp from call_data limit 100",
     features=["callcenter:waitduration"],
)

dataset = store.create_saved_dataset(
    from_=historicalJob,
    name='callcenter_training',
    storage=SavedDatasetPostgreSQLStorage("test2")
)

print(dataset.to_df())