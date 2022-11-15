from feast import FeatureStore
from feast.infra.offline_stores.file_source import SavedDatasetFileStorage
from feast.infra.offline_stores.contrib.postgres_offline_store.postgres_source import SavedDatasetPostgreSQLStorage
import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

store = FeatureStore(repo_path="../definitions")

# Get the latest feature values for unique entities
historicalJob = store.get_historical_features(
    entity_df="select id, closing_time as event_timestamp from call_data limit 100",
     features=["callcenter:wait_duration"],
)

dataset = store.create_saved_dataset(
    from_=historicalJob,
    name='callcenter-linear_training',
    storage=SavedDatasetPostgreSQLStorage("test4")
)

print(dataset.to_df())