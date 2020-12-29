import numpy as np

#Option 1
dict_a = {'a':[100,np.nan,np.nan,200]}
import pandas as pd
df = pd.DataFrame(dict_a)

print("Data type with float datatype ")
"""
It will be float as there is null, one of the most important concept in python
if there is null then it will be float as np.nan is float

We are going to convert this float datatype to string along without impacting null.
if you will directly convert it to str with astype then np.nan will be as string'nan'
Below trick is to convert 'nan' to np.nan
"""
print(df)

df['a'] = df['a'].astype('Int64')   
df['a'] =df['a'].astype('str') 
df['a'] = df['a'].apply(lambda x:str(x) if x != 'nan' else np.nan)
print(df)

#Option 2
#this step is to analysis to get the above solution

dict_a = {'a':[100,np.nan,np.nan,200]}
import pandas as pd
df = pd.DataFrame(dict_a)


print(df)
df['a'] =df['a'].astype('str') 
for data in df['a']:
    
    print(data=='nan')
