import os
import pandas as pd
from src.train_model import load_data, train_and_evaluate

DATA_PATH = os.path.join("data", "global_cancer_patients_2015_2024.csv")


def test_load_data():
    df = load_data(DATA_PATH)
    # basic assertions
    assert not df.empty, "DataFrame should not be empty"
    assert "Year" in df.columns and "Patients" in df.columns


def test_train_and_evaluate_returns_mse():
    df = load_data(DATA_PATH)
    model, mse = train_and_evaluate(df)
    # model should have coef_ attribute
    assert hasattr(model, "coef_")
    # MSE should be a non-negative float
    assert isinstance(mse, float)
    assert mse >= 0.0
