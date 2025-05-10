import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from typing import Tuple


def load_data(path: str) -> pd.DataFrame:
    """Load CSV into a DataFrame."""
    return pd.read_csv(path)


def train_and_evaluate(df: pd.DataFrame) -> Tuple[LinearRegression, float]:
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


if __name__ == "__main__":
    # change this path if needed
    DATA_PATH = "data/global_cancer_patients_2015_2024.csv"
    df = load_data(DATA_PATH)
    _, mse = train_and_evaluate(df)
    print(f"Trained LinearRegression on {len(df)} samples → MSE: {mse:.2f}")
