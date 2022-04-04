import pandas as pd


df=pd.read_excel('0.xlsx',skiprows=1)
df=df.drop('Zeit',axis=1)
columns=df.columns
cols = df.select_dtypes(exclude=['float']).columns

df[cols] = df[cols].apply(pd.to_numeric, downcast='float', errors='coerce')
print(df.dtypes)

