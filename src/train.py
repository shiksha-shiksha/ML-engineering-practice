import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

filepath = "data/raw/gallstone.csv"
if not Path(filepath).is_file():
    raise FileNotFoundError(
        f"Dataset file not found: {filepath}. Run src/get_data.py first"
    )

data = pd.read_csv(filepath)
X = data.drop(columns=["Gallstone Status"])
y = data["Gallstone Status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

Path("artifacts").mkdir(exist_ok=True)
joblib.dump(model, "artifacts/model.pkl")
with open("artifacts/metrics.json", "w") as f:
    json.dump({"accuracy": accuracy}, f, indent=4)
print(f"Accuracy: {accuracy:.4f}")
