import requests
api_key = ""

twilio_code = ""

parameters = {
    "lat": "29.760427",
    "lon": "-95.369804",
    "cnt": 4,
    "appid": api_key
}

response = requests.get(url = "https://api.openweathermap.org/data/2.5/forecast", params = parameters)
response.raise_for_status()
data = response.json()

#print(data)
#print(data["list"][0]["weather"][0]["id"])

will_rain = False

for increment in range(0,4):
    condition_code = data["list"][increment]["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella.")



