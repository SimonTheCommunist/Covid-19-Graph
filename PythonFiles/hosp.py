import json
import requests
import matplotlib.pyplot as plt
import numpy as np
url = "https://covidtracking.com/api/v1/us/daily.json"
response = requests.get(url)
json_data = response.json()

x, x2 = [], []
y = []
start, end = 0, 159
i=0

if start < end:
    y.extend(range(start, end))
    y.append(end)

for i in response.json():
    x.append(i["hospitalizedCurrently"])
    x2.append(i["hospitalizedCumulative"])

x2.reverse()
x.reverse()

plt.plot(y, x, label = "hospitalized currently")
plt.plot(y, x2, label = "Cumulative Hospitalizations")
plt.ylabel('number of hospitalized people')
plt.xlabel('days since Jan 22, 2020')
plt.title('COVID-19 by the days')
plt.legend()
plt.show()




