import pandas as pd
import sys
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score 
from sklearn.pipeline import Pipeline


###############################################
# Load the dataset and split it into training and testing sets
###############################################
df = pd.read_csv("/home/yash/ML/Customer_Churn_Prediction/data/customer_churn_prediction_dataset.csv")
df = df.drop(columns=["customerID"])
x_train, x_test, y_train, y_test = train_test_split(df.drop(columns=["Churn"]), df["Churn"], test_size=0.2,random_state=0)


################################################
# Import the Preprocessing_data class from the preprocessing module
################################################

# Add project root to Python's module search path
sys.path.append("/home/yash/ML/Customer_Churn_Prediction")

# Import your preprocessing class
from preprocessing.Preprocessing import Preprocessing_function

pf = Preprocessing_function()

################################################
# Apply Logistic Regression and Preprocessing using Pipline 
################################################

lr = LogisticRegression()

ct = Pipeline(
    [
    ("Preprocessing",pf),
    ("LogisticRegression",lr)
    ]
)

ct.fit(x_train,y_train)

################################################
# Predict y_pred by x_test & find accuracy score 
################################################

y_pred = ct.predict(x_test)

################################################
# Dump Pipline as Pickel file 
################################################

print(accuracy_score(y_true=y_test, y_pred=y_pred)*100)

with open ("Customer_Churn_Prediction/model/model.pkl","wb") as file:
    pickle.dump(ct,file)
    
print("\nModel saved successfully..!!")