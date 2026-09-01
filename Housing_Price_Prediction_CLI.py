# -------------------------------------------------------------------
# Import Library
# -------------------------------------------------------------------

import pandas as pd
import pickle


# -------------------------------------------------------------------
# Taking Input
# -------------------------------------------------------------------

print("\n")
print("="*50)
print("            House🏠 Price💰 Prediction")
print("="*50,"\n")

# House Area
while True:
    house_area = input("📐 Enter Sqft Area of House : ").strip()
    try:
        house_area = float(house_area)
        break
    except ValueError:
        print("Invalid Input Please Enter Sqft Area of House Again..!!")
print("")

# Bedroom     
while True:
    Bedrooms = input("🛏️  Enter Number Bedrooms of House : ").strip()
    try:
        Bedrooms = float(Bedrooms)
        break
    except ValueError:
        print("Invalid Input Please Enter Number Bedrooms of House Again..!!")
print("")

# Bathroom
while True:
    Bathrooms = input("🛁 Enter Number Bathrooms of House : ").strip()
    try:
        Bathrooms = float(Bathrooms)
        break
    except ValueError:
        print("Invalid Input Please Enter Number Bathrooms of House Again..!!")
print("")
  
# Floors              
while True:
    Floors = input("🏢 Enter Floors of House : ").strip()
    try:
        Floors = float(Floors)
        break
    except ValueError:
        print("Invalid Input Please Enter Floors of House Again..!!")
print("")

# Garage
while True:
    garage = input("🚗 Enter Numbers of Garage in House : ").strip()
    try:
        garage = float(garage)
        break
    except ValueError:
        print("Invalid Input Please Enter Numbers of Garage in House Again..!!")
print("")

# Distance
while True:
    distance = input("🏙️  Enter Distance from city of House : ").strip()
    try:
        distance = float(distance)
        break
    except ValueError:
        print("Invalid Input Please Enter Distance from city of House Again..!!")
print("")

# Condition
while True:
    condition = input("⭐ Rate a Condition House out of 5 : ").strip()
    try:
        condition = float(condition)
        if 0 <= condition <= 5:
            break
        else:
            print("Please enter a value between 0 and 5.")
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 5.")
print("")

# Location
while True:
    Location = input("📍 Enter Location of House(Suburban,Urban,Rural) : ").title().strip()
    if Location == "Suburban" or Location == "Urban" or Location == "Rural":
        break
    else:
        print("Invalid Input Please Enter Suburban or Urban or Rural.")
print("")

# Garden
while True:
    garden = input("🌳 Enter Numbers of Garden in House : ").strip()
    try:
        garden = float(garden)
        break
    except ValueError:
        print("Invalid Input Please Enter Numbers of Garden in House Again..!!")
print("")

# Pool
while True:
    pool = input("🏊 Enter Numbers of Pool in House : ").strip()
    try:
        pool = float(pool)
        break
    except ValueError:
        print("Invalid Input Please Enter Numbers of Garage in House Again..!!")
print("")

# Parking
while True:
    parking = input("🅿️  Enter Numbers of Parking in House : ").strip()
    try:
        parking = float(parking)
        break
    except ValueError:
        print("Invalid Input Please Enter Numbers of Parking in House Again..!!")
print("")

# Built Year
while True:
    year = input("📅 Enter Year Built of House : ").strip()
    try:
        year = float(year)
        break
    except ValueError:
        print("Invalid Input Please Enter Year Built of House Again..!!")
print("")


# -------------------------------------------------------------------
# Save All input in data
# -------------------------------------------------------------------

data = {
    "area_sqft"             : house_area,
    "bedrooms"              : Bedrooms,
    "bathrooms"             : Bathrooms,
    "floors"                : Floors,
    "garage"                : garage,
    "distance_from_city_km" : distance,
    "condition"             : condition,
    "location"              : Location,
    "has_garden"            : garden,
    "has_pool"              : pool,
    "parking"               : parking,
    "year_built"            : year
}

data = pd.DataFrame(data,index = [0])


# -------------------------------------------------------------------
# Import Model and Load it
# -------------------------------------------------------------------

with open("model.pkl", "rb") as file:
    model_data = pickle.load(file)

pipeline = model_data["Pipeline"]

y = pipeline.predict(data) # Predict


# -------------------------------------------------------------------
# Print Prediction and others 
# -------------------------------------------------------------------

print("-"*50)
print("                    Prediction")
print("-"*50,"\n")
print(f"Predicted Value of Your House is : ₹{int(y[0])} 💵","\n")
print("-"*50)
print("\nMAE       :  1549559.8337291332\nMSE       :  3668453649925.448\nR2-Score  :  98.2980882745605 %")
print("\n","-"*50)