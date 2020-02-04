import pandas as pd
import numpy as np
import datetime as dt
from bs4 import BeautifulSoup
import datetime
import requests
import json


#Flask API URL
url = 'http://127.0.0.1:5000'

#For debugging purposes
date = datetime.datetime.now()

#Simplify Date
year = date.year
month = date.month
day = date.day

#Get avg_temp automatically
response = requests.get("https://api.wunderground.com/history/airport/KSFO/" + str(year) + "/" + str(month) + "/" + str(day) + "/DailyHistory.html")
if(response.ok):
    data = response.text
    soup = BeautifulSoup(data)
    values = soup.find_all("span", class_="wx-value")
    values = [x.get_text() for x in values]
    avg_temp = values[0]

#Get day of week automatically

#Loop for all PdDistricts

#Get NFL game? automatically
#Data
data = { 'avg_temp': int(avg_temp),
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

#data = data.to_json()
data = json.dumps(data)

send_request = requests.post(url, data)
print(send_request)
print(send_request.json())
