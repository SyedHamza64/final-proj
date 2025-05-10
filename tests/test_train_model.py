# ─── at the bottom of tests/test_train_model.py ────────────────────────────────

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression


def train_cancer_type_classifier(df: pd.DataFrame):
    """
    Train a LogisticRegression to predict Cancer_Type from Year (toy example).
    Returns the fitted classifier and its LabelEncoder.
    """
    X = df[['Year']]                     # feature(s) for demo
    y = df['Cancer_Type']
    le = LabelEncoder().fit(y)
    y_enc = le.transform(y)
    clf = LogisticRegression(max_iter=200).fit(X, y_enc)
    return clf, le


def test_sample_leukemia_prediction():
    # A single-row sample matching your specification:
    sample = {
        'Patient_ID': 'PT0000001',
        'Age': 34,
        'Gender': 'Male',
        'Country_Region': 'China',
        'Year': 2021,
        'Genetic_Risk': 1.3,
        'Air_Pollution': 4.5,
        'Alcohol_Use': 3.7,
        'Smoking': 3.9,
        'Obesity_Level': 6.3,
        'Cancer_Type': 'Leukemia',
        'Cancer_Stage': 'Stage 0',
        'Treatment_Cost_USD': 12573.41,
        'Survival_Years': 4.7,
        'Target_Severity_Score': 4.65,
    }
    df_sample = pd.DataFrame([sample])

    # Train & predict
    clf, le = train_cancer_type_classifier(df_sample)
    pred_label = le.inverse_transform(clf.predict(df_sample[['Year']]))[0]

    # Assert the classifier gets ‘Leukemia’
    assert pred_label == 'Leukemia'
