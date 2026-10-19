import pandas as pd
import sys
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score 


###############################################
# Load the dataset and split it into training and testing sets
###############################################
df = pd.read_csv("/home/yash/ML/Customer_Churn_Prediction/data/customer_churn_prediction_dataset.csv")
df = df.drop(columns=["customerID"])
x_train, x_test, y_train, y_test = train_test_split(df.drop(columns=["Churn"]), df["Churn"], test_size=0.2)


################################################
# Import the Preprocessing_data class from the preprocessing module
################################################

# Add project root to Python's module search path
sys.path.append("/home/yash/ML/Customer_Churn_Prediction")

# Import your preprocessing class
from preprocessing.Preprocessing import Preprocessing_data

preprocessing = Preprocessing_data(x_train, x_test)
preprocessing.missing_values()
preprocessing.Scaling()
preprocessing.Encoding() 
x_train, x_test = preprocessing.Get_Processed_Data()


################################################
# Train the Logistic Regression model
################################################

model = LogisticRegression()
model.fit(x_train, y_train) 


###############################################
# Predict for x_test and finds the accuracy score
###############################################

y_pred = model.predict(x_test)
print(accuracy_score(y_test,y_pred)*100)

with open("Customer_Churn_Prediction/model/model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved successfully!")
