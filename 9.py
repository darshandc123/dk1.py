import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/SPTINT-17/Desktop/dataset/titanic (1).csv")
print(data)
plt.xlabel("Survived")
plt.ylabel("Pclass")

plt.scatter(data['Survived'],data['Pclass'])
plt.show()

plt.plot(data['Survived'])
plt.plot(data['Fare'])
plt.show()

plt.bar(data['Survived'],data['Pclass'])
plt.show()

plt.hist(data['Fare'])
plt.show()
plt.pie(data['Fare'])
plt.show()

