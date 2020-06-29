import json
import requests
import matplotlib.pyplot as plt

url = "https://covidtracking.com/api/v1/us/daily.json"
response = requests.get(url)
json_data = response.json()




y = []
start, end = 0, 158
if start < end:
    y.extend(range(start, end))
    y.append(end)
i=0
x = []

for i in response.json():
    x.append(i["positive"])

x.reverse()
plt.plot(y, x)
plt.ylabel('number of infections')
plt.xlabel('days since Jan 22, 2020')
plt.title('COVID-19 by the days')
plt.show()





