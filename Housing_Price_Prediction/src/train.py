# -------------------------------------------------------------------
# Import All Library which we needed
# -------------------------------------------------------------------

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression,Ridge
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pickle


# -------------------------------------------------------------------
# Load Data from Downloads Folder
# -------------------------------------------------------------------


df = pd.read_csv("/home/yash/ML/Housing_Price_Prediction/data/house_price_prediction_dataset_3000_fixed.csv")
df = df.drop(columns = ["age_years"])


# -------------------------------------------------------------------
# Fill missing values in DataFrame 
# -------------------------------------------------------------------

# Fill all missing value in Garage and conditon column by "0" and by median
df["garage"] = df["garage"].fillna("0")
df["condition"] = df["condition"].fillna(df["condition"].median())


# Fill all missing value in Bathrooms column by predicting it's value 
x = df.drop(columns=["price_inr"])
y = df["price_inr"]

# Split known data for training and missing data for predict their value 

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=0
)# Remove Price column to save data leakage 

bathroom_train = x_train[x_train["bathrooms"].notna()]
bathroom_missing_train = x_train[x_train["bathrooms"].isna()]
bathroom_x_train = bathroom_train.drop(columns=["bathrooms"])
bathroom_y_train = bathroom_train["bathrooms"]
bathroom_x_pred = bathroom_missing_train.drop(columns=["bathrooms"])

bathroom_x_train = bathroom_x_train.drop(columns=["location"])
bathroom_x_pred = bathroom_x_pred.drop(columns=["location"])

lr = LogisticRegression(max_iter=1000)

lr.fit(bathroom_x_train, bathroom_y_train)

bathroom_predictions = lr.predict(bathroom_x_pred)

x_train.loc[x_train["bathrooms"].isna(),"bathrooms"] = bathroom_predictions

bathroom_test_missing = x_test[x_test["bathrooms"].isna()]

bathroom_test_x_pred = bathroom_test_missing.drop(columns=["bathrooms", "location"])

test_bathroom_predictions = lr.predict(bathroom_test_x_pred)

x_test.loc[x_test["bathrooms"].isna(),"bathrooms"] = test_bathroom_predictions


# ----------------------------------------------------------------------------------------------------
# Apply Ordinal Encoding to convert categorical data in to numerical and StandardScaler to Scale data
# ----------------------------------------------------------------------------------------------------

trf = ColumnTransformer(
    transformers=[
        ("Encoding",OneHotEncoder(),[7]),
        ("Scale",StandardScaler(),[0,5,11])
        ],
    remainder="passthrough")


# -------------------------------------------------------------------
# Make Pipline 
# -------------------------------------------------------------------

Pipeline = Pipeline([
     ("trf1",trf),
     ("Ridge",Ridge(alpha=14))
    ])


# -------------------------------------------------------------------
# Apply Pipeline 
# -------------------------------------------------------------------

Pipeline.fit(x_train,y_train)


# -------------------------------------------------------------------
# Save a Model 
# -------------------------------------------------------------------

model_data = {
    "Pipeline" : Pipeline
}

with open("Housing_Price_Prediction/model/model.pkl", "wb") as file:
    pickle.dump(model_data, file)

print("\nModel saved successfully!")


# -------------------------------------------------------------------
# Predict Output and find R2 Score
# -------------------------------------------------------------------

y_pred = pd.DataFrame(Pipeline.predict(x_test))
print("MAE       : ",mean_absolute_error(y_test,y_pred))
print("MSE       : ",mean_squared_error(y_test,y_pred))
print("R2-Score  : ",r2_score(y_test,y_pred)*100,"%")