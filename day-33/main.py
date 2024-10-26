import requests
from datetime import datetime


# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# response.raise_for_status()
#
# longitude =response.json()["iss_position"]["longitude"]
# latitude =response.json()["iss_position"]["latitude"]
#
# iss_position = (longitude,latitude)
#
# print(iss_position)

MY_LAT = 30.267153
MY_LNG = -97.743057

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0

}

response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()

data = response.json()

# print(data)
# print(data["results"])

# sunrise = (data["results"]["sunrise"])
# sunset = (data["results"]["sunset"])

time_now = datetime.now()

# print(sunrise)
# print(sunrise.split("T"))
# print(sunrise.split("T")[1].split(":"))
# print(sunrise.split("T")[1].split(":")[0])

print(data["results"]["sunrise"])

sunrise = ((data["results"]["sunrise"]).split("T")[1].split(":")[0])
sunset = ((data["results"]["sunset"]).split("T")[1].split(":")[0])

print(sunrise)
print(sunset)

print(time_now.hour)

