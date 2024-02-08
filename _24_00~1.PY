import json
from datetime import datetime
import requests, os, time

# setting up environment variables:
APP_ID = os.environ.get('APP_ID', 'APP_ID does not exist')
API_KEY = os.environ.get('API_KEY', 'API_KEY does not exist')
AUTHORIZATION_BEARER_TOKEN = os.environ.get('AUTHORIZATION_BEARER_TOKEN', 'AUTHORIZATION_BEARER TOKEN does not exist')

# Print statements for environment variables (for debugging purposes):
print(f"The APP_ID is: {APP_ID}")
print(f"The API_KEY is: {API_KEY}")
print(f"The AUTHORIZATION_BEARER_TOKEN is: {AUTHORIZATION_BEARER_TOKEN}")

gender = "male"
weight_in_kg = "75.8"
height_in_cm = "179"
age = 40

# Encrypt the following in Env Vars:
# Toggle off or on, depending on Commiting or not: (if toggled off for the actual password, then toggle on the Env Vars and ensure Env Vars work, then just remove your actual password entirely from the code:

#------------------ Nutritionix Territory -----------------#
# host domain: https://trackapi.nutritionix.com
exercise_endpoint_url = "https://trackapi.nutritionix.com/v2/natural/exercise"   #MY ACTUAL ENDPOINT.

#-----------------  Sheety Territory -----------------#
sheety_endpoint_url = "https://api.sheety.co/61ebfea22e49232bb280d6a22d698d26/sirisWorkouts/workouts"

# to use bearer Tokens:
sheety_headers = {
    "Authorization": f"Bearer {AUTHORIZATION_BEARER_TOKEN}",
    "Content-Type": "application/json"
}

exercise_text = input("Please tell me which exercises you did Today, and the duration of each (if you know): ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": gender,
    "weight_kg": weight_in_kg,
    "height_cm": height_in_cm,
    "age": age,
}

exercise_response = requests.post(url=exercise_endpoint_url, json=parameters, headers=headers)
exercise_result = exercise_response.json()
print(exercise_result)

date_and_time_now = datetime.now()
print(date_and_time_now)

now_formatted_date = date_and_time_now.strftime("%d/%m/%Y")
print(now_formatted_date)

now_formatted_time = date_and_time_now.strftime("%H:%M:%S")   #same thing as: print(date_and_time_now.strftime("%X"))
print(now_formatted_time)

# TODO1: You will be using strftime()

# TODO: APIs and Making POST Requests

# TODO: Authorization Headers

# TODO: Environment Variables

for each_exercise in exercise_result['exercises']:  # exercises = exercise_result['exercises']
    json_payload_sheet_inputs = {
        'workout' : {
            "date" : now_formatted_date,
            "time" : now_formatted_time,
            "exercise": each_exercise['name'].title(),
            "duration": each_exercise['duration_min'],  # in minutes
            "calories": each_exercise['nf_calories'],  # in kcal
        }
    }
    sheety_post_request_response = requests.post(url=sheety_endpoint_url, json=json_payload_sheet_inputs, headers=sheety_headers)
    print(sheety_post_request_response.text)
