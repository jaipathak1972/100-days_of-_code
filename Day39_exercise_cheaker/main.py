import requests
from datetime import datetime

# Replace placeholders with your actual information
GENDER = "male"  # Replace with your gender: "male" or "female"
WEIGHT_KG = 70.5  # Replace with your weight in kilograms
HEIGHT_CM = 175  # Replace with your height in centimeters
AGE = 25  # Replace with your age

# Replace with your Nutritionix Application ID and API Key
APP_ID = "eefa43a8"
API_KEY = "01eac0c667a35dc8d0f90ac81c05cefe"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/1817f12a19f3d263d917342dc4c33ef3/myWorkouts/sheet1"  # Replace with your Sheety endpoint

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")



for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)
