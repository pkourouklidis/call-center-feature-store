from feast import FeatureStore
import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#setup the credentials needed to access the minio bucket
os.environ["AWS_SECRET_ACCESS_KEY"] = "minio123"
os.environ["AWS_ACCESS_KEY_ID"] = "minio"
os.environ["FEAST_S3_ENDPOINT_URL"] = "http://minio-service.kubeflow.svc.cluster.local:9000"

store = FeatureStore(repo_path=".")

# Get the latest feature values for unique entities
entity_df = pd.DataFrame.from_dict({"callID": [0, 1, 2, 3, 4],})
entity_df["event_timestamp"] = pd.to_datetime("now", utc=True)
training_df = store.get_historical_features(
    entity_df=entity_df, features=["callFeatures:waitDuration"],
).to_df()


# Make batch predictions
# predictions = model.predict(training_df)
print(training_df)