from feast import FeatureStore
import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#setup the credentials needed to access the minio bucket
os.environ["AWS_SECRET_ACCESS_KEY"] = "minio123"
os.environ["AWS_ACCESS_KEY_ID"] = "minio"
os.environ["FEAST_S3_ENDPOINT_URL"] = "http://localhost:9000"

store = FeatureStore(repo_path=".")
dataset = store.get_saved_dataset('callcenter_training')
print(dataset.to_df())