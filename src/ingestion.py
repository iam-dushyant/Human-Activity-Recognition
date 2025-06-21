import pandas as pd
import os
import yaml

CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.yaml')
with open(CONFIG_PATH, 'r') as f:
    config = yaml.safe_load(f)

raw_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), config['data']['raw_path'])
df = pd.read_csv(raw_path)
print("Ingested data shape:", df.shape)
