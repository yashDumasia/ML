###########################################
# Import all which are needed Libreries 
###########################################

import streamlit as st
import pandas as pd
import pickle

###########################################
# Web Title & Sub-title
###########################################

st.title("📊 Customer Churn Prediction 📊")
st.subheader("🤖 Machine Learning Powered • Customer Retention Insights")

###########################################
st.divider()

###########################################
# Taking All Inputs
###########################################
 
# gender, SeniorCitizen, Partner, Dependents, PhoneService & OnlineSecurity
cols0,cols1,cols2,cols3,cols4,cols5 = st.columns(6)
with cols0:
    gender = st.radio("Gender 👤 :",["Male","Female"])
with cols1:
    SeniorCitizen = st.radio("SeniorCitizen👴 :",["Yes","No"])
    if SeniorCitizen == "Yes":
        SeniorCitizen = 1
    else:
        SeniorCitizen = 0
with cols2:
    Partner = st.radio("Has Partner 💑 :",["Yes","No"])
with cols3:
    Dependents = st.radio("Dependents 👨‍👩‍👧 :",["Yes","No"])
with cols4:
    PhoneService = st.radio("Phone Service 📱 :",["Yes","No"])
with cols5:
    OnlineSecurity = st.radio("Online Security🔐 :",["Yes","No"])

# tenure, MultipleLines, InternetService & OnlineBackup
cols0,cols1,cols2,cols3,cols4 = st.columns(5)
with cols0:
    tenure = st.number_input("Tenure (in years) 📅 :",min_value=0,max_value=100)
with cols1:
    MultipleLines = st.radio("MultipleLines ☎️ :",["Yes","No","No phone service"])
with cols2:
    InternetService = st.radio("InternetService 🌐 :",["DSL", "Fiber optic", "No"])
with cols3:
    OnlineBackup = st.radio("Online Backup ☁️ :",["Yes","No","No phone service"])
with cols4:
    DeviceProtection = st.radio("Device Protection 🛡️ :",["Yes","No","No phone service"])

# TechSupport, StreamingTV, StreamingMovies, Contract & PaperlessBilling
cols0,cols1,cols2,cols3,cols4 = st.columns(5)
with cols0:
    TechSupport = st.radio("Tech Support 🧑‍💻 :",["Yes","No"])
with cols1:
    StreamingTV = st.radio("Streaming TV 📺 :",["Yes","No","No phone service"] )
with cols2:
    StreamingMovies = st.radio("Streaming Movies 🎬 :",["Yes","No","No phone service"] )
with cols3:
    Contract = st.radio("Contract 📝 :",["Month-to-month","Two year","One year"])
with cols4:
    PaperlessBilling = st.radio("Paperless Billing 📄 :",["Yes","No"])

# PaymentMethod, MonthlyCharges & TotalCharges
cols0,cols1,cols2 = st.columns(3)
with cols0:
    PaymentMethod = st.radio("PaymentMethod 💳 :", ["Bank transfer","Electronic check","Credit card","Mailed check"])
with cols1:
    MonthlyCharges = st.number_input("MonthlyCharges 💵 :",min_value=0, max_value=1000)
with cols2:
    TotalCharges = st.number_input("TotalCharges 🧾 :",min_value=0,max_value=10000)

###########################################
st.divider()
        
###########################################
# Predict Button & Predict Output
###########################################

if st.button("Predict Customer Churn"):
    customer_data = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [SeniorCitizen],
        "Partner": [Partner],
        "Dependents": [Dependents],
        "tenure": [tenure],
        "PhoneService": [PhoneService],
        "MultipleLines": [MultipleLines],
        "InternetService": [InternetService],
        "OnlineSecurity": [OnlineSecurity],
        "OnlineBackup": [OnlineBackup],
        "DeviceProtection": [DeviceProtection],
        "TechSupport": [TechSupport],
        "StreamingTV": [StreamingTV],
        "StreamingMovies": [StreamingMovies],
        "Contract": [Contract],
        "PaperlessBilling": [PaperlessBilling],
        "PaymentMethod": [PaymentMethod],
        "MonthlyCharges": [MonthlyCharges],
        "TotalCharges": [TotalCharges],
    })

    # Load model from model/model.pkl 
    with open("Customer_Churn_Prediction/model/model.pkl", "rb") as file:
        model = pickle.load(file)

    prediction = model.predict(customer_data)[0]

    if prediction == "Yes":
        st.error("⚠️ There are 78.17 % chance that the Customer will Churn.")
    else:
        st.success("✅ There are 78.17 % chance that the Customer will not Churn.")
