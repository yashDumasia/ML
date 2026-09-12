import streamlit as st
import pandas as pd
import pickle 

st.title("House🏠 Price💰 Prediction")

st.divider()


Area = st.number_input("📐 Enter Sqft Area of House :",min_value=300,max_value=50000,value=1500)

cols1, cols2 = st.columns(2)
with cols1:
    Bedroom = st.number_input("🛏️  Enter Number Bedrooms of House :",min_value=1,max_value=20,value=2)
with cols2:
    Bathroom = st.number_input("🛁 Enter Number Bathrooms of House :",min_value=1,max_value=20,value=2)
    
cols1, cols2 = st.columns(2) 
with cols1:
    Floor = st.number_input("🏢 Enter Floors of House :",min_value=0,max_value=200)
with cols2:
    Garage = st.number_input("🚗 Enter Numbers of Garage in House :",min_value=0,max_value=10)
    
cols1, cols2 = st.columns(2)
with cols1:
    Distance = st.number_input("🏙️  Enter Distance from city of House(km) :",min_value=0)
with cols2:
    Condition = st.number_input("⭐ Rate a Condition House out of 5 :",min_value=0.0,max_value=5.0,step=0.05,value=2.5)
    
cols1,cols2,cols3,cols4 = st.columns(4)
with cols1:
    Location = st.radio("📍 Location :",["Suburban","Urban","Rural"])
with cols2:
    Garden = st.radio("🌳 Has Garden :",["Yes","No"])
with cols3:
    Pool = st.radio("🏊 Has Pool :",["Yes","No"])
with cols4:
    Parking = st.radio("🅿️ Has Parking :",["Yes","No"])

cols1,cols2,cols3= st.columns(3)
with cols1:
    Built_year = st.number_input("📅 Enter Year Built of House :",min_value=1900,max_value=2026,value=2000)

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

    st.divider()


    st.success(f"Predicted Value of Your House is : ₹{int(y[0])} 💵")
    
    st.divider()
    
    cols1, cols2 = st.columns(2)
    with cols1:
        st.metric("MAE :","1.444*10^6")
    with cols2:
        st.metric("MSE :","3.241*10^12")

    cols3, cols4 = st.columns(2)
    with cols3:
        st.metric("R2-Score :","98.50 %")
    with cols4:
        st.metric("Cross Validation R² :","98.59 %")
    
    st.divider()
        
    st.markdown("Predicted House Value is Depend on training data.")