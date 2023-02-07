import os

from feast import FeatureStore
from feast.infra.offline_stores.contrib.postgres_offline_store.postgres_source import (
    SavedDatasetPostgreSQLStorage,
)

os.chdir(os.path.dirname(os.path.abspath(__file__)))

store = FeatureStore(repo_path="../definitions")

# Get the latest feature values for unique entities
historicalJob = store.get_historical_features(
    entity_df="select id, ts as event_timestamp from stt order by event_timestamp desc limit 100",
    features=[
        "stt:input",
        "stt:prediction",
        "stt:label",
    ],
)

dataset = store.create_saved_dataset(
    from_=historicalJob,
    name="stt_training",
    storage=SavedDatasetPostgreSQLStorage("stt_saved"),
)

print(dataset.to_df())
