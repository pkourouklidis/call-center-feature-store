import os

from feast import FeatureStore
from feast.infra.offline_stores.contrib.postgres_offline_store.postgres_source import (
    SavedDatasetPostgreSQLStorage,
)
import numpy as np
from psycopg2.extensions import register_adapter, AsIs


def addapt_numpy_array(numpy_array):
    stringRepresentation = ",".join(str(element) for element in numpy_array)
    return AsIs("'{" + stringRepresentation + "}'")


register_adapter(np.ndarray, addapt_numpy_array)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

store = FeatureStore(repo_path="../definitions")

# Get the latest feature values for unique entities
historicalJob = store.get_historical_features(
    entity_df="select id, ts as event_timestamp from credit order by event_timestamp desc limit 100",
    features=[
        "credit:sex",
        "credit:credit_prediction",
        "credit:credit_label",
    ],
)

dataset = store.create_saved_dataset(
    from_=historicalJob,
    name="credit-nb_training",
    storage=SavedDatasetPostgreSQLStorage("credit_saved"),
)

print(dataset.to_df())

