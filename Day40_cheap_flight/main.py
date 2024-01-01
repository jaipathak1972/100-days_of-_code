#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


import requests

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint

sheetAPI = "https://api.sheety.co/1817f12a19f3d263d917342dc4c33ef3/flightDeals/sheet1"
response = requests.get(sheetAPI)
sheet_data = response.json()['sheet1']
