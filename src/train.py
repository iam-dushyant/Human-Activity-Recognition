from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib
import yaml
import os

with open(os.path.join("config", "config.yaml")) as f:
    config = yaml.safe_load(f)

data = pd.read_csv(config['data']['processed_path'])
X = data.drop('target', axis=1)
y = data['target']

model = RandomForestClassifier(**config['model']['params'])
model.fit(X, y)

joblib.dump(model, config['model']['save_path'])
