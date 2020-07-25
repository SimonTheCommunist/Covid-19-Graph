import json
import requests
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import r2_score
import math
import numpy

url = "https://covidtracking.com/api/v1/us/daily.json"
response = requests.get(url)
json_data = response.json()
#----------------------------------------------
y, x, x2, x3, x4 = [], [], [], [], []
i =0
start, end = 0, 184

#----------------------------------------------

if start < end:
    y.extend(range(start, end))
    y.append(end)

for i in response.json():
    x.append(i["positive"])
    #x2.append(i["negative"])
    #x3.append(i["totalTestResults"])
    #x4.append(i["totalTestResultsIncrease"])
#----------------------------------------------

x.reverse()

mymodel = numpy.poly1d(numpy.polyfit(y, x, 3))


myline = numpy.linspace(1, 220, 100)

r2 = (1.0 + (r2_score(mymodel(x), y)))
day215 = mymodel(215)
predday215 = math.floor(day215)

plt.xlabel("days since January 22")
plt.ylabel("positive test results")

plt.title('Positive COVID-19 with Regression')
plt.scatter(y, x, label = "positive test results")
lines = plt.plot(myline, mymodel(myline)) 
plt.setp(lines, color='r', linewidth=2.0)
plt.plot(myline, mymodel(myline), label = "polynomial regression line") 
plt.scatter(215, predday215, label = "predicted cases at day 215: " + str(predday215))
plt.grid(True)
plt.annotate("r2 = " + str(r2), xy=(15, 4300000))
plt.annotate("current date: July 24, 2020", xy=(15, 4100000))
plt.annotate("August 24, 2020", xy=(215, predday215), xytext=(150, 5000000), arrowprops=dict(facecolor='black')) 
plt.legend()
plt.show() 

