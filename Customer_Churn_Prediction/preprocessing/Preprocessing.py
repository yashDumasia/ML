from sklearn.preprocessing import MinMaxScaler,OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pandas as pd

# Numerical features
NUMERIC_COLUMNS = [
    "SeniorCitizen",
    "tenure",
    "MonthlyCharges",
    "TotalCharges",
]

# Categorical features
CATEGORICAL_COLUMNS = [
    "gender",
    "Partner",
    "Dependents",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
]

def Preprocessing_function():
    
    numerical_transformer = Pipeline([
            ("SimpleImputer", SimpleImputer(strategy="median")),
            ("MinMaxScaler", MinMaxScaler())
            ]
    )

    categorical_transformer = Pipeline([
            ("SimpleImputer", SimpleImputer(strategy="most_frequent")),
            ("OneHotEncoder", OneHotEncoder(handle_unknown="ignore"))
            ]
    )

    preprocessor = ColumnTransformer([
        ("numeric", numerical_transformer, NUMERIC_COLUMNS),
        ("categorical", categorical_transformer, CATEGORICAL_COLUMNS),
    ])
    
    return preprocessor
