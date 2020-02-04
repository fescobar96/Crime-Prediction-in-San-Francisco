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
    soup = BeautifulSoup(data, features='lxml')
    values = soup.find_all("span", class_="wx-value")
    values = [x.get_text() for x in values]
    avg_temp = values[0]

#Get day of week automatically
wd = date.weekday()
week = [0,0,0,0,0,0]

if wd == 1:
    week[0] = 1
elif wd == 2:
    week[1] = 1
elif wd == 3:
    week[2] = 1
elif wd == 4:
    week[3] = 1
elif wd == 5:
    week[4] = 1
elif wd == 6:
    week[5] = 1



#Loop for all PdDistricts

#Get NFL game? automatically
#Data
data = { 'avg_temp': int(avg_temp),
         'Day': int(day),
         'Month': int(month),
         'Year': int(year),
         'PdDistrict_CENTRAL': 0,
         'PdDistrict_INGLESIDE': 0,
         'PdDistrict_MISSION': 0,
         'PdDistrict_NORTHERN': 0,
         'PdDistrict_PARK': 0,
         'PdDistrict_RICHMOND': 0,
         'PdDistrict_SOUTHERN': 0,
         'PdDistrict_TARAVAL': 0,
         'PdDistrict_TENDERLOIN': 0,
         'DayOfWeek_Monday': week[0],
         'DayOfWeek_Saturday': week[4],
         'DayOfWeek_Sunday': week[5],
         'DayOfWeek_Thursday': week[3],
         'DayOfWeek_Tuesday': week[1],
         'DayOfWeek_Wednesday': week[2],
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
