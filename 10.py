import pandas as pd 
import numpy as np
dict={'first number':[10,20,np.nan],
                      'second number':[20,np.nan,50],
                      'thirt number':[np.nan,20,60]}
data=pd.DataFrame(dict)
print(data)
print(data.isnull())
print(data.notnull())
print(data.dropna(how="all"))
#print(data.fillna(10))
#print(data.fillna(method='bfill'))
print(data.fillna(method='pad'))
