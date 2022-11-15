from feast import FeatureStore
import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

store = FeatureStore(repo_path="../definitions")
dataset = store.get_saved_dataset('callcenter-linear_training')
print(dataset.to_df())