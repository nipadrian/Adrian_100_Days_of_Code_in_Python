import requests
from datetime import datetime
from pprint import pprint
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_DOMAIN = "https://api.sheety.co/561665c6db0847b0f34c1293296bac10/flightDeals/prices"




class DataManager:
    #This class is responsible for talking to the Google Sheet.
    # SHEETY_HEADERS = {
    #     "Authorization": SHEETY_KEY
    # }
    # SHEETY_KEY = os.environ["SHEETY_KEY"]
    # SHEETY_HEADERS = {
    #     "Authorization": os.environ["SHEETY_KEY"]
    # }

    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        #self._user = SHEETY_USERNAME
        #self._password = SHEETY_KEY
        #self.authorization = (self._user, self._password)
        self._password = os.environ["SHEETY_KEY"]
        self.authorization = HTTPBasicAuth(self._user,self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url = SHEETY_DOMAIN, auth = self.authorization)#, auth = (self._user,self._password))
        sheet_data = response.json()
        pprint(sheet_data)
        self.destination_data = sheet_data["prices"]
        pprint(sheet_data)
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url = f"{SHEETY_DOMAIN}/{city['id']}",
                auth = self.authorization,
                #auth=(self._user, self._password),
                json = new_data

            )
            print(response.text)