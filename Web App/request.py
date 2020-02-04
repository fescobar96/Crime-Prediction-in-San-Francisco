import pandas as pd
import numpy as np
import datetime as dt
import requests
import json


#Flask API URL
url = 'http://127.0.0.1:5000'

#Data
data = { 'avg_temp': 14,
         'Day': 6,
         'Month': 1,
         'Year': 2003,
         'PdDistrict_CENTRAL': 0,
         'PdDistrict_INGLESIDE': 0,
         'PdDistrict_MISSION': 0,
         'PdDistrict_NORTHERN': 0,
         'PdDistrict_PARK': 0,
         'PdDistrict_RICHMOND': 0,
         'PdDistrict_SOUTHERN': 0,
         'PdDistrict_TARAVAL': 0,
         'PdDistrict_TENDERLOIN': 0,
         'DayOfWeek_Monday': 1,
         'DayOfWeek_Saturday': 0,
         'DayOfWeek_Sunday': 0,
         'DayOfWeek_Thursday': 0,
         'DayOfWeek_Tuesday': 0,
         'DayOfWeek_Wednesday': 0,
         'NFL_Game_Day_1': 0,
         }

#Preprocess Data
#data = pd.DataFrame(data, index=[0])
#data['Dates'] = pd.to_datetime(data['Dates'])
#data['Day'] = data['Dates'].dt.day
#data['Month'] = data['Dates'].dt.month
#data['Year'] = data['Dates'].dt.year
#data.drop(columns=['Dates'], inplace=True)
#data = pd.get_dummies(data, columns=["PdDistrict", "DayOfWeek", "NFL_Game_Day"], drop_first=True)
#data = data[['Day']]

print()
#data = data.to_json()
data = json.dumps(data)

send_request = requests.post(url, data)
print(send_request)
print(send_request.json())
