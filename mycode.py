import pandas as pd
import os

data={'name':['Alice','bob','charlie'],
      'age':[25,30,35],
      'city':['New York','Los Angeles', 'chicago']
      }


df=pd.DataFrame(data)
new_row={'name':"mahi",'age':34,'city':'Dhaka'}
df.loc[len(df.index)]=new_row

df.to_csv(r'./data/data.csv')