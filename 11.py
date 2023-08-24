import pandas as pd 
data=pd.read_csv("C:/Users/SPTINT-17/Desktop/dataset/auto-mpg (1).csv")
#stats=data.describe()
#print(stats)
#c=data[data['cylinders']==8][['car name','cylinders']]
#print(c)
c=data.groupby('model year')['model year'].count()
print(c)
