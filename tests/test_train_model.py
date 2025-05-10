# tests/test_train_model.py

import os

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# ─── model code merged from src/train_model.py ───────────────────────────────

def load_data(path: str) -> pd.DataFrame:
    """Load CSV into a DataFrame."""
    return pd.read_csv(path)


def train_and_evaluate(df: pd.DataFrame):
    """
    Train a simple year→patients linear model and return (model, MSE).
    Expects columns 'Year' and 'Patients'.
    """
    X = df[['Year']].values.reshape(-1, 1)
    y = df['Patients'].values
    model = LinearRegression()
    model.fit(X, y)
    preds = model.predict(X)
    mse = mean_squared_error(y, preds)
    return model, mse


# ──────────────────────────────────────────────────────────────────────────────


DATA_PATH = os.path.join("data", "global_cancer_patients_2015_2024.csv")


def test_load_data():
    df = load_data(DATA_PATH)
    assert not df.empty, "DataFrame should not be empty"
    assert "Year" in df.columns and "Patients" in df.columns


def test_train_and_evaluate_returns_mse():
    df = load_data(DATA_PATH)
    model, mse = train_and_evaluate(df)
    assert hasattr(model, "coef_"), "Model should have coef_ attribute"
    assert isinstance(mse, float), "MSE should be a float"
    assert mse >= 0.0, "MSE should be non-negative"
