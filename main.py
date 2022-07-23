import requests
import os
from datetime import datetime

#app is nutritionix.com
id_nutritionix = os.environ.get("ID_NUTRITIONIX")
key_nutritionix = os.environ.get("KEY_NUTRITIONIX")
endpoint_nutritionix = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": id_nutritionix,
    "x-app-key": key_nutritionix,
}

exercise_params = {
 "query": f"{input('What exercises did you do today?: ')}",
 "gender": "male",
 "weight_kg": 73.0,
 "height_cm": 180.34,
 "age": 27
}

response = requests.post(url=endpoint_nutritionix, json=exercise_params, headers=headers)
results = response.json()

####################################################################

sheet_name = "your_sheet_name"
project_name = "yourSheetName"
username = "site_provided_username"
sheety_bearer_token = os.environ.get("SHEETY_TOKEN")
sheety_endpoint = os.environ.get("SHEETY_WORKOUT_ENDPOINT")

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime(f"'%X'")

excel_header = {
    "Authorization": f"Bearer {sheety_bearer_token}"
}

for exercise in results["exercises"]:
    excel_data = {
        "workout":
            {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
            }
    }
    sheety_response = requests.post(url=sheety_endpoint, json=excel_data, headers=excel_header)

# sheety_response2 = requests.get(url=sheety_endpoint, headers=excel_header)
# sheety_response2.json()
