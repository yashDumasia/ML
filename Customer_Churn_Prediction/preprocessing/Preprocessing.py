from sklearn.preprocessing import MinMaxScaler,OneHotEncoder
import pandas as pd

class Preprocessing_data:
    
    def __init__(self,x_train,x_test):
        self.x_train = x_train.drop(columns=["customerID"], errors='ignore')
        self.x_test = x_test.drop(columns=["customerID"], errors='ignore')


    ###########################################
    # Handling Missing Values
    ###########################################
    def missing_values(self):

        # In Traning Data
        self.x_train["OnlineBackup"] = self.x_train["OnlineBackup"].fillna("No")
        self.x_train["TechSupport"] = self.x_train["TechSupport"].fillna("No")
        self.x_train["TotalCharges"] = self.x_train["TotalCharges"].fillna(self.x_train["TotalCharges"].median())

        # In Testing Data
        self.x_test["OnlineBackup"] = self.x_test["OnlineBackup"].fillna("No")
        self.x_test["TechSupport"] = self.x_test["TechSupport"].fillna("No")
        self.x_test["TotalCharges"] = self.x_test["TotalCharges"].fillna(self.x_test["TotalCharges"].median())


    ############################################
    # Scaling
    ############################################
    def Scaling(self):

        # Min-Max Scaling
        mms = MinMaxScaler()
        self.x_train[["tenure","MonthlyCharges","TotalCharges"]] = mms.fit_transform(self.x_train[["tenure","MonthlyCharges","TotalCharges"]])
        self.x_test[["tenure","MonthlyCharges","TotalCharges"]] = mms.transform(self.x_test[["tenure","MonthlyCharges","TotalCharges"]])


    ############################################
    # Encoding      
    ############################################
    def Encoding(self):
        
        # Categorical columns
        cat_cols = [
            "gender", "Partner", "Dependents", "PhoneService",
            "MultipleLines", "InternetService", "OnlineSecurity",
            "OnlineBackup", "DeviceProtection", "TechSupport",
            "StreamingTV", "StreamingMovies", "Contract",
            "PaperlessBilling", "PaymentMethod"
        ]

        # One Hot Encoding
        ohe = OneHotEncoder(sparse_output=False, drop="first")

        # Fit on training data
        train_encoded = pd.DataFrame(
            ohe.fit_transform(self.x_train[cat_cols]),
            columns=ohe.get_feature_names_out(cat_cols),
            index=self.x_train.index
        )

        # Transform testing data using the same encoder
        test_encoded = pd.DataFrame(
            ohe.transform(self.x_test[cat_cols]),
            columns=ohe.get_feature_names_out(cat_cols),
            index=self.x_test.index
        )

        # Remove original categorical columns
        self.x_train = self.x_train.drop(columns=cat_cols)
        self.x_test = self.x_test.drop(columns=cat_cols)

        # Combine numerical and encoded categorical columns
        self.x_train = pd.concat(
            [self.x_train, train_encoded], axis=1
        )

        self.x_test = pd.concat(
            [self.x_test, test_encoded], axis=1
        )
        
        
    ############################################
    # Return Processed Data
    ############################################
    def Get_Processed_Data(self):
        
        # Return 
        return self.x_train, self.x_test