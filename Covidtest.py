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
x2 = []
x3 = []
x4= []

for i in response.json():
    x.append(i["positive"])
for i in response.json():
    x2.append(i["negative"])
for i in response.json():
    x3.append(i["totalTestResults"])
for i in response.json():
    x4.append(i["totalTestResultsIncrease"])

x.reverse()
x2.reverse()
x3.reverse()
x4.reverse()
plt.plot(y, x, label="Positive Test Results")
#plt.plot(y, x2, label="Negative Test Results")
plt.plot(y, x3, label="Total Test Results")
#plt.plot(y, x4, label="Total Test Results Increase")
plt.ylabel('Number of test results in milions')
plt.xlabel('days since Jan 22, 2020')
plt.title('COVID-19 by the days')
#plt.xlim(100, 160)
#plt.ylim(0, 10000)
plt.legend()
plt.show()