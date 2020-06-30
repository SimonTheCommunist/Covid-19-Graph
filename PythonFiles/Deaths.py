import json
import requests
import matplotlib.pyplot as plt

url = "https://covidtracking.com/api/v1/us/daily.json"
response = requests.get(url)
json_data = response.json()
#----------------------------------------------
y, x, x2, x3, x4, x5, x6, x7 = [], [], [], [], [], [], [], []
i =0
start, end = 0, 159

#----------------------------------------------

if start < end:
    y.extend(range(start, end))
    y.append(end)

for i in response.json():
    x.append(i["positive"])
    x2.append(i["negative"])
    x3.append(i["totalTestResults"])
    x4.append(i["totalTestResultsIncrease"])
    x5.append(i["deathIncrease"])
    x6.append(i["death"])
    x7.append(i["states"])
#----------------------------------------------

x.reverse()
x2.reverse()
x3.reverse()
x4.reverse()
x5.reverse()
x6.reverse()
x7.reverse()

#plt.plot(y, x, label="Positive Test Results")
#plt.plot(y, x2, label="Negative Test Results")
#plt.plot(y, x3, label="Total Test Results")
#plt.plot(y, x4, label="Total Test Results Increase")
#plt.plot(y, x5, label="New Deaths")
#plt.plot(y, x6, label="Total Deaths")
plt.plot(y, x7, Label="States or US Territory with a positve case")


plt.ylabel('Number of States or US Territory with a positve case')
plt.xlabel('days since Jan 22, 2020')

plt.title('COVID-19 by the days')
#plt.xlim(100, 160)
#plt.ylim(0, 10000)
plt.legend()
plt.show()