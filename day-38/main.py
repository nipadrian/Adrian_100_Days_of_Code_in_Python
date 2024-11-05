import requests
from datetime import datetime
import os


NUTRITION_ID = ""
NUTRITION_KEY = ""

# os.environ["NUTRITION_ID"] = "1e49aa58"
# os.environ["NUTRITION_KEY"] = NUTRITION_KEY

host_domain = "https://trackapi.nutritionix.com"
endpoint = "/v2/natural/exercise"

# os.environ["host_domain"] = host_domain
# os.environ["endpoint"] = endpoint

headers = {
    "x-app-id": NUTRITION_ID,
    "x-app-key": NUTRITION_KEY
}

params = {
    "query" : input("Input your exercise.")
}

#print (query)
response = requests.post(url = host_domain + endpoint, json = params, headers = headers)
print(response.text)

now = datetime.now()
date = now.strftime("%m/%d/%Y")
time = now.strftime("%H:%M:%S")
exercise = (response.json()["exercises"][0]["name"])
duration = (response.json()["exercises"][0]["duration_min"])
calories = (response.json()["exercises"][0]["nf_calories"])


sheety_domain = ""

sheety_key = ""

sheety_headers = {
    "Authorization": sheety_key
}

sheety_input = {
    "workout" : {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

sheety_post = requests.post(url = sheety_domain, json = sheety_input, headers = sheety_headers)
print(sheety_post.text)