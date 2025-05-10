# ─── code from src/train_model.py ──────────────────────────────
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from typing import Tuple

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def train_and_evaluate(df: pd.DataFrame) -> Tuple[LinearRegression, float]:
    X = df[['Year']].values.reshape(-1, 1)
    y = df['Patients'].values
    model = LinearRegression().fit(X, y)
    preds = model.predict(X)
    mse = mean_squared_error(y, preds)
    return model, mse
# ───────────────────────────────────────────────────────────────

# ─── your tests below ─────────────────────────────────────────
import os

DATA_PATH = os.path.join("data", "global_cancer_patients_2015_2024.csv")

def test_load_data():
    df = load_data(DATA_PATH)
    assert not df.empty
    assert "Year" in df.columns and "Patients" in df.columns

def test_train_and_evaluate_returns_mse():
    df = load_data(DATA_PATH)
    model, mse = train_and_evaluate(df)
    assert hasattr(model, "coef_")
    assert isinstance(mse, float) and mse >= 0
# ───────────────────────────────────────────────────────────────
