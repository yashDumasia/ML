################################################
# Import all Library which are needed 
################################################

from rich.console import Console
import pandas as pd
import pickle

################################################
# Take all inputs 
################################################

c = Console()
c.print("="*75, style="bold dark_green")
c.print("                     #######################################", style="bold bright_white")
c.print("                     ### 📊 Customer Churn Prediction 📊 ###", style="bold bright_white")
c.print("                     #######################################", style="bold bright_white")
c.print("="*75,"\n", style="bold dark_green")
c.print("👋 Welcome to Customer Churn Prediction System..!!\n",style="yellow1")
c.print("-"*75,"\n", style="bold dark_green")

# gender
while True:
    gender = input("Enter Gender 👤 of customer(for Male M and for Female F) : ").strip().upper()
    if gender == "M" or gender == "F":
        if gender == "M":
            gender = "Male"
        else:
            gender = "Female"
        break
    else:
        c.print("❌  Invalid Input Please Enter Gender Again..!!  ❌", style="bold bright_red")
print("")

# SeniorCitizen
while True:
    SeniorCitizen = input("Is customer seniorcitizen 👴 or not(Yes or No (Y/N)) : ").strip().upper()
    if SeniorCitizen == "Y" or SeniorCitizen == "N":
        if SeniorCitizen == "Y":
            SeniorCitizen = 1
        else:
            SeniorCitizen = 0
        break
    else:
        c.print("❌  Invalid Input Please Enter Seniorcitizen Again..!!  ❌", style="bold bright_red")
print("")

# Partner  
while True:
    Partner = input("Is customer has partner 💑 or Not (Yes or No (Y/N)) : ").strip().upper()
    if Partner == "Y" or Partner == "N":
        if Partner == "Y":
            Partner = "Yes"
        else :
            Partner = "No"
        break
    else:
        c.print("❌  Invalid Input Please Enter Partner Again..!!  ❌", style="bold bright_red")
print("")

# Dependents
while True:
    Dependents = input("Is Customer Dependent 👨‍👩‍👧 or Not (Yes or No (Y/N)) : ").strip().upper()
    if Dependents == "Y" or Dependents == "N":
        if Dependents == "Y":
            Dependents = "Yes"
        else :
            Dependents = "No"
        break
    else:
        c.print("❌  Invalid Input Please Enter Dependent Again..!!  ❌", style="bold bright_red")
print("")

# Tenure
while True:
    try:
        tenure = int(input("Enter Customer Tenure 📅 (in years) : ").strip())
        break
    except ValueError:
        c.print("❌  Invalid Input Please Enter Tenure Again..!!  ❌", style="bold bright_red")
print("")

# PhoneService
while True:
    PhoneService = input("Is Customer Have Phoneservice 📱 or Not (Yes or No (Y/N)) : ").strip().upper()
    if PhoneService == "Y" or PhoneService == "N":
        if PhoneService == "Y":
            PhoneService = "Yes"
        else:
            PhoneService = "No"
        break
    else:
        c.print("❌  Invalid Input Please Enter Phoneservice Again..!!  ❌", style="bold bright_red")
print("")

# MultipleLines
while True:
    MultipleLines = input("Is Customer Have Multiple Lines ☎️  or Not or No phone service (Yes or No (Y/N/NPS)) : ").strip().upper()
    if MultipleLines == "Y" or MultipleLines == "N" or MultipleLines == "NPS":
        if MultipleLines == "Y":
            MultipleLines = "Yes"
        elif MultipleLines == "N":
            MultipleLines = "No"
        elif MultipleLines == "NPS":
            MultipleLines = "No phone service"
        break
    else:
        c.print("❌  Invalid Input Please Enter Multiple Lines Again..!!  ❌", style="bold bright_red")      
print("")

# InternetService
while True:
    InternetService = input("Choose Internet Service 🌐 (DSL, Fiber optic, No) : ").strip()
    if InternetService in ["DSL", "Fiber optic", "No"]:
        break
    else:
        c.print("❌  Invalid Input Please Enter Internet Service Again..!!  ❌", style="bold bright_red")
print("")

# OnlineSecurity
while True:
    OnlineSecurity = input("Is OnlineSecurity 🔐 Available or Not (Yes or No (Y/N)) : ").strip().upper()
    if OnlineSecurity == "Y" or OnlineSecurity == "N":
        if OnlineSecurity == "Y":
            OnlineSecurity = "Yes"
        else:
            OnlineSecurity = "No"
        break
    else:
        c.print("❌  Invalid Input Please Enter Online Security Again..!!  ❌", style="bold bright_red")
print("")

# OnlineBackup
while True:
    OnlineBackup = input("Is OnlineBackup ☁️ Available or Not or No internet service(Yes or No or No internet service (Y/N/NIS)) : ").strip().upper()
    if OnlineBackup == "Y" or OnlineBackup == "N" or OnlineBackup == "NIS":
        if OnlineBackup == "Y":
            OnlineBackup = "Yes"
        elif OnlineBackup == "N":
            OnlineBackup = "No"
        elif OnlineBackup == "NIS":
            OnlineBackup = "No internet service"
        break
    else:
        c.print("❌  Invalid Input Please Enter Online Backup Again..!!  ❌", style="bold bright_red")
print("")

# DeviceProtection
while True:
    DeviceProtection = input("Is Devic Protection 🛡️  Available or Not or No internet service(Yes or No or No internet service (Y/N/NIS)) : ").strip().upper()
    if DeviceProtection == "Y" or DeviceProtection == "N" or DeviceProtection == "NIS":
        if DeviceProtection == "Y":
            DeviceProtection = "Yes"
        elif DeviceProtection == "N":
            DeviceProtection = "No"
        elif DeviceProtection == "NIS":
            DeviceProtection = "No internet service"
        break
    else:
        c.print("❌  Invalid Input Please Enter Device Protection Again..!!  ❌", style="bold bright_red")
print("")

# TechSupport
while True:
    TechSupport = input("Is Tech Support 🧑‍💻 Available or Not (Yes or No (Y/N)) : ").strip().upper()
    if TechSupport == "Y" or TechSupport == "N":
        if TechSupport == "Y":
            TechSupport = "Yes"
        else:
            TechSupport = "No"
        break
    else:
        c.print("❌  Invalid Input Please Enter Tech Support Again..!!  ❌", style="bold bright_red")
print("")

# StreamingTV
while True:
    StreamingTV = input("Is StreamingTV 📺 Available or Not or No internet service (Yes or No or No internet service (Y/N/NIS)) : ").strip().upper()
    if StreamingTV == "Y" or StreamingTV == "N" or StreamingTV == "NIS":
        if StreamingTV == "Y":
            StreamingTV = "Yes"
        elif StreamingTV == "N":
            StreamingTV = "No"
        elif StreamingTV == "NIS":
            StreamingTV = "No internet service"
        break
    else:
        c.print("❌  Invalid Input Please Enter Streaming TV Again..!!  ❌", style="bold bright_red")
print("")

# StreamingMovies                                                       
while True:
    StreamingMovies = input("Is Streaming Movies 🎬 Available or Not or No internet service (Yes or No or No internet service (Y/N/NIS)) : ").strip().upper()
    if StreamingMovies == "Y" or StreamingMovies == "N" or StreamingMovies == "NIS":
        if StreamingMovies == "Y":
            StreamingMovies = "Yes"
        elif StreamingMovies == "N":
            StreamingMovies = "No"
        elif StreamingMovies == "NIS":
            StreamingMovies = "No internet service"
        break
    else:
        c.print("❌  Invalid Input Please Enter Streaming Movies Again..!!  ❌", style="bold bright_red")
print("")

# Contract
while True:
    Contract = input("Contract 📝 (Month-to-month(M2M), Two year(2Y), One year(1Y)) : ").strip().upper()
    if Contract == "M2M" or Contract == "2Y" or Contract == "1Y":
        if Contract == "M2M":
            Contract = "Month-to-month"
        elif Contract == "2Y":
            Contract = "Two year"
        elif Contract == "1Y":
            Contract = "One year"
        break
    else:
        c.print("❌  Invalid Input Please Enter Contract Again..!!  ❌", style="bold bright_red")
print("")

# PaperlessBilling
while True:
    PaperlessBilling = input("Is PaperlessBilling 📄 Available or Not (Yes or No (Y/N)) : ").strip().upper()
    if PaperlessBilling == "Y" or PaperlessBilling == "N":
        if PaperlessBilling == "Y":
            PaperlessBilling = "Yes"
        else:
            PaperlessBilling = "No"
        break
    else:
        c.print("❌  Invalid Input Please Enter Paperless Billing Again..!!  ❌", style="bold bright_red")
print("")

# PaymentMethod
while True:
    PaymentMethod = input("Payment Method 💳 (Bank transfer (BT), Electronic check (EC), Credit card (CC), Mailed check (MC)) : ").strip().upper()
    if PaymentMethod == "BT" or PaymentMethod == "EC" or PaymentMethod == "CC" or PaymentMethod == "MC":
        if PaymentMethod == "BT":
            PaymentMethod = "Bank transfer"
        elif PaymentMethod == "EC":
            PaymentMethod = "Electronic check"
        elif PaymentMethod == "CC":
            PaymentMethod = "Credit card"
        elif PaymentMethod == "MC":
            PaymentMethod = "Mailed check"
        break
    else:
        c.print("❌  Invalid Input Please Enter Payment Method Again..!!  ❌", style="bold bright_red")
print("")

# MonthlyCharges
while True:
    MonthlyCharges = input("Enter Monthly Charges 💵 : ").strip()
    try:
        MonthlyCharges = float(MonthlyCharges)
        break
    except ValueError:
        c.print("❌  Invalid Input Please Enter Monthly Charges Again..!!  ❌", style="bold bright_red")
print("")

# TotalCharges
while True:
    TotalCharges = input("Enter Total Charges 🧾 : ").strip()
    try:
        TotalCharges = float(TotalCharges)
        break
    except ValueError:
        c.print("❌  Invalid Input Please Enter Total Charges Again..!!  ❌", style="bold bright_red")
print("")

################################################
# Convert all inputs in DataFrame 
################################################

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

################################################ 
# Load Model and predict Output
################################################

with open ("Customer_Churn_Prediction/model/model.pkl","rb") as file:
    model = pickle.load(file)

if model.predict(customer_data) == "No":
    c.print("There are 78.17 % chance that the Customer will Churn.",style="Red1")
else :
    c.print("There are 78.17 % chance that the Customer will not Churn.",style="Green1")
    