from feast import FeatureStore, RepoConfig
from feast.infra.offline_stores.file import FileOfflineStore
from feast.infra.offline_stores.file_source import FileSource
import pandas as pd
import os
import datetime

from pytz import utc

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#setup the credentials needed to access the minio bucket
os.environ["AWS_SECRET_ACCESS_KEY"] = "minio123"
os.environ["AWS_ACCESS_KEY_ID"] = "minio"
os.environ["FEAST_S3_ENDPOINT_URL"] = "http://minio-service.kubeflow.svc.cluster.local:9000"

store = FeatureStore(repo_path=".")

ds = store.get_data_source("callcenterSource")
job = FileOfflineStore.pull_all_from_table_or_query(config=store.config,
    data_source=ds, join_key_columns=['callID'], timestamp_field=ds.timestamp_field,
    feature_name_columns=['waitDuration', 'serviceDuration'],
    start_date=datetime.datetime(2022,1,1,tzinfo=utc), end_date=datetime.datetime.now(tz=utc))

print(job.to_df())

fv = store.get_feature_view("callFeatures")
print(fv.features[0].name)
print(fv.entities)
print(type(fv.batch_source))
if type(fv.batch_source)==FileSource:
    print('FileSource')
joinKeys = [item for sublist in [store.get_entity(x).join_keys for x in fv.entities] for item in sublist]
print(joinKeys)