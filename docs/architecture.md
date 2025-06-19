# Architecture Overview

1. Data ingestion reads `train.csv` and validates schema.
2. Preprocessing cleans nulls, scales features, and encodes categories.
3. Feature engineering adds domain-specific variables.
4. Training script builds a RandomForest model.
5. The model is evaluated and saved to `models/model.pkl`.
6. A Flask API exposes predictions using the trained model.
