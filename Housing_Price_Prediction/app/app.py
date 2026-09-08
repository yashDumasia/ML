import streamlit as st
import pandas as pd
import pickle 

st.title("House🏠 Price💰 Prediction")


Area = st.number_input("📐 Enter Sqft Area of House :",min_value=300)
Bedroom = st.slider("🛏️  Enter Number Bedrooms of House :",1,20)
Bathroom = st.slider("🛁 Enter Number Bathrooms of House :",1,20)
Floor = st.slider("🏢 Enter Floors of House :",0,200)
Garage = st.slider("🚗 Enter Numbers of Garage in House :",0,10)
Distance = st.number_input("🏙️  Enter Distance from city of House(km) :",min_value=0)
Condition = st.number_input("⭐ Rate a Condition House out of 5 :",min_value=0.0,max_value=5.0)
Location = st.radio("📍 Location :",["Suburban","Urban","Rural"])
Garden = st.radio("🌳 Has Garden :",["Yes","No"])
Pool = st.radio("🏊 Has Pool :",["Yes","No"])
Parking = st.radio("🅿️ Has Parking :",["Yes","No"])
Built_year = st.number_input("📅 Enter Year Built of House :",min_value=1900,max_value=2026)
if st.button("Predict Price"):
    if Garden == "Yes":
        Garden = 1
    else:
        Garden = 0
        
    if Pool == "Yes":
        Pool = 1
    else:
        Pool = 0
        
    if Parking == "Yes":
        Parking = 1
    else:
        Parking = 0
        
    data = {
    "area_sqft"             : Area,
    "bedrooms"              : Bedroom,
    "bathrooms"             : Bathroom,
    "floors"                : Floor,
    "garage"                : Garage,
    "distance_from_city_km" : Distance,
    "condition"             : Condition,
    "location"              : Location,
    "has_garden"            : Garden,
    "has_pool"              : Pool,
    "parking"               : Parking,
    "year_built"            : Built_year
    }
    
    data = pd.DataFrame(data,index = [0])
    
    with open("Housing_Price_Prediction/model/model.pkl", "rb") as file:
        model_data = pickle.load(file)

    pipeline = model_data["Pipeline"]

    y = pipeline.predict(data) # Predict

    st.success(f"Predicted Value of Your House is : ₹{int(y[0])} 💵")
    st.success("MAE : 1444996.2531460086\n\n"
               "MSE : 3241236366888.3535\n\n"
               "R2-Score : 98.49628789017403 %\n\n"
               "Cross Validation R² : 98.59268268002552 % \n\n")
