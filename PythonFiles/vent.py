import json
import requests
import matplotlib.pyplot as plt
import numpy as np
url = "https://covidtracking.com/api/v1/us/daily.json"
response = requests.get(url)
json_data = response.json()




y, x, x2, x3 = [], [], [], []
start, end = 0, 159
i = 0


if start < end:
    y.extend(range(start, end))
    y.append(end)

for i in response.json():
    x.append(i["onVentilatorCurrently"])
    x2.append(i["inIcuCurrently"])
    #x3.append(i["positive"])
    #x2.append(i["onVentilatorCumulative"])

x3.reverse()
x2.reverse()
x.reverse()
plt.plot(y, x, label = "People Currently on ventilator")
plt.plot(y, x2, label = "People Currently in ICU")
#plt.plot(y, x3, label = "Number tested positive")
plt.ylabel('number of people ')
plt.xlabel('days since Jan 22, 2020')
plt.title('COVID-19 by the days')
plt.legend()
plt.show()