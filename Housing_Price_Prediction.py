# Import All Library which we have needed
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression,Ridge
from sklearn.preprocessing import StandardScaler,OrdinalEncoder
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score


# Taking Data from Downloads

df = pd.read_csv("/home/yash/Downloads/house_price_prediction_dataset_3000_fixed.csv")
df = df[["area_sqft","bedrooms","bathrooms","age_years","floors","location","price_inr"]] # Chosing Column on which ml model apply


# Fill missing values in DataFrame 

# Fill all missing value in Location column by "Missing" word
df["location"] = df["location"].fillna("Missing")

# Fill all missing value in Bathrooms column by predicting it's value 
train_data = df[df["bathrooms"].notna()]
missing_data = df[df["bathrooms"].isna()]

x_train = train_data.drop(columns=["bathrooms"])
y_train = train_data["bathrooms"]
x_pred = missing_data.drop(columns=["bathrooms"])
y_pred = missing_data["bathrooms"] # Split value for prediction

lr = LogisticRegression()
lr.fit(x_train.drop(columns=["location"]),y_train) # apply logistic regrssion for predict missing values
 
y_pred = lr.predict(x_pred.drop(columns=["location"])) # predict missing values 
df.loc[df['bathrooms'].isna(), 'bathrooms'] = y_pred # add predict values in dataframe 


# Split Dataframe 

x_train,x_test,y_train,y_test = train_test_split(df.drop(columns=["price_inr"]),df["price_inr"],test_size=0.2,random_state=0)


# Apply Ordinal Encoding to convert categorical data in to numerical 

ohe = OrdinalEncoder(categories=[['Missing', 'Rural', 'Urban', 'Suburban']])

ohe.fit(x_train[["location"]])
x_train["location"] = ohe.transform(x_train[["location"]])
x_test["location"] = ohe.transform(x_test[["location"]])

x_train = pd.DataFrame(x_train)
x_test = pd.DataFrame(x_test)


# Apply StandardScaler to Scale data

ss = StandardScaler()

x_train[["area_sqft","bedrooms","bathrooms","age_years","floors","location"]] = ss.fit_transform(x_train)
x_test[["area_sqft","bedrooms","bathrooms","age_years","floors","location"]] = ss.transform(x_test)


# Apply Ridge with alpha 15 to train a model 

r = Ridge(alpha = 15)
r.fit(x_train,y_train)

print("\n")
print("="*50)
print("              House Price Prediction")
print("="*50,"\n")

while True:
    house_area = input("Enter Sqft Area of House : ")
    try:
        house_area = float(house_area)
        break
    except ValueError:
        print("Invalid Input Please Enter Sqft Area of House Again..!!")
print("")
       
while True:
    Bedrooms = input("Enter Number Bedrooms of House : ")
    try:
        Bedrooms = float(Bedrooms)
        break
    except ValueError:
        print("Invalid Input Please Enter Number Bedrooms of House Again..!!")
print("")

while True:
    Bathrooms = input("Enter Number Bathrooms of House : ")
    try:
        Bathrooms = float(Bathrooms)
        break
    except ValueError:
        print("Invalid Input Please Enter Number Bathrooms of House Again..!!")
print("")
        
while True:
    Age = input("Enter Age of House(Years) : ")
    try:
        Age = float(Age)
        break
    except ValueError:
        print("Invalid Input Please Enter Age of House Again..!!")
print("")
        
while True:
    Floors = input("Enter Floors of House : ")
    try:
        Floors = float(Floors)
        break
    except ValueError:
        print("Invalid Input Please Enter Floors of House Again..!!")
print("")

while True:
    Location = input("Enter Location of House(Suburban,Urban,Rural) : ").title()
    if Location == "Suburban" or Location == "Urban" or Location == "Rural":
        break
    else:
        print("Invalid Input Please Enter Suburban or Urban or Rural.")
print("")

data = {
    "area_sqft" : house_area,
    "bedrooms"  : Bedrooms,
    "bathrooms" : Bathrooms,
    "age_years" : Age,
    "floors"    : Floors,
    "location"  : Location
}

data = pd.DataFrame(data,index = [0])
data["location"] = ohe.transform(data[["location"]])
data[["area_sqft","bedrooms","bathrooms","age_years","floors","location"]] = ss.transform(data)

y = r.predict(data)
print(f"Predicted Value of Your House is : {y}Rs.")

# Predict Output and find R2 Score

y_pred = pd.DataFrame(r.predict(x_test))
print("\nAccuracy Score of House Prediction is : ",r2_score(y_test,y_pred)*100)