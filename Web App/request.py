import pandas as pd
import numpy as np
import datetime as dt
import requests
import json



url = 'http://127.0.0.1:5000'

# sample data
data = {'Dates': 3,
        'PdDistrict': 2,
        'DayOfWeek': 1,
        'avg_temp': 50,
        'NFL_Game_Day': 0
        }

data = pd.DataFrame(data, index=[0])
data['Dates'] = pd.to_datetime(data['Dates'])
data['Day'] = data['Dates'].dt.day
data['Month'] = data['Dates'].dt.month
data['Year'] = data['Dates'].dt.year
data.drop(columns=['Dates'], inplace=True)

data = json.dumps(data)

send_request = requests.post(url, data)
print(send_request)
