import pandas as pd
df=pd.read_csv("C:/Users/SPTINT-17/Desktop/data/iris.csv")
print(df)

print(df.head(5))

print(df.tail(2))

print(df["Species"])

print(df.info())

print(df.count())                                                                                                                              
