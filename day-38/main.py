import requests

NUTRITION_ID = "1e49aa58"
NUTRITION_KEY = "ba8228bb02ed6c2335642607c693b62c"

host_domain = "https://trackapi.nutritionix.com"
endpoint = "/v2/natural/exercise"

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