import requests
from datetime import datetime
from pprint import pprint

sheety_domain = "https://api.sheety.co/561665c6db0847b0f34c1293296bac10/flightDeals/prices"
sheety_key = "Basic bnVsbDpudWxs"

sheety_headers = {
    "Authorization": sheety_key
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    sheety_get = requests.get(url = sheety_domain, headers = sheety_headers)
    #pprint(sheety_get.text)
    prices = sheety_get.text
    print(prices)
    print(prices["prices"])
