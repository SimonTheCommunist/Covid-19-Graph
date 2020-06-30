import json
import requests
import matplotlib.pyplot as plt
import numpy as np

#---------------------------------------------------------------
#API STUFF
url = "https://covidtracking.com/api/v1/us/daily.json"
response = requests.get(url)
json_data = response.json()

#END OF API STUFF-----------------------------------------------
#START OF DATA STUFF--------------------------------------------
i=0
x2, y2 = [], []
y, x = [], []
start, end = 0, 159
start2, end2 = 159, 204

#makes an array for y values. Time.
if start < end:
    y.extend(range(start, end))
    y.append(end)

#makes an array positive test results
for i in response.json():
    x.append(i["positive"])

#makes an array for days being used by the prediction
if start2 < end2:
    y2.extend(range(start2, end2))
    y2.append(end2)

#uses exponetial growth to predict how the chart will change
for i in range(8, 54):
    x2.append((2300193*(1.01432** i)))
#reverse the data to be logical.
x.reverse()
x2_ = np.array(x2)
y2_ = np.array(y2)

#print(x)
#print(x2)
plt.plot(y, x)
plt.plot(y2_, x2_, label="predicted")
plt.ylabel('number of infections')
plt.xlabel('days since Jan 22, 2020')
plt.title('COVID-19 by the days')
plt.legend()
plt.show()



