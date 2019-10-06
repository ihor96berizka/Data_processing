import requests
import json

import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data_2019-9-01_to_2019-9-30.json'

payload = {'device': 'Il/C', 'startDate': '2019-9-01', 'endDate': '2019-9-30', 'properties': 'temperature'}
response = requests.get("https://yz58i1wove.execute-api.eu-west-1.amazonaws.com"
                "/dev/data/group-by/hour", params=payload)

print('response info')
print(response.url)
print(response.status_code)
jsonRecv = response.json()

print('save json to file')\

with open(filename, "w") as write_file:
    json.dump(jsonRecv, write_file)

#print(jsonRecv)
'''
with open(filename, "r") as read_file:
    jsonRecv = json.load(read_file)

print('jsonRecv type: ', type(jsonRecv))
'''
dates = []
temperature = []

for item in jsonRecv:
    date = datetime.strptime(item['hour'], '%Y-%m-%d %H:%M:%S.%f')
    dates.append(date)
    temperature.append(float(item['temperature']) / 100.0)
    #print('date: ', item['hour'])

print('len(dates)= ', len(dates))
print('type(dates) = ', type(temperature[0]))

data = dict(zip(dates, temperature))
print('dict: ')
print(data)
print('items in dict: ')
print(len(data))

# A list of the keys of dictionary
list_keys = [k for k in data]

# or a list of the values
list_values = [v for v in data.values()]


def plotting():
    plt.subplot(1, 1, 1)
    plt.plot(list_keys, list_values)
    plt.title('Sensors readings')
    plt.ylabel('temperature, C')
    plt.show()


plotting()