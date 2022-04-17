import pandas as pd
import os
path=os.path.dirname(__file__)
files=os.listdir(path)
index=[]
mean_list=[]
columns=None
for file in files:
    if file.endswith(".xlsx"):
        index.append(file.split('.')[0])
        fname=os.path.join(path,file)
        df=pd.read_excel(fname,skiprows=1)
        df=df.drop('Zeit',axis=1)
        df=df.fillna(0)
        cols = df.select_dtypes(exclude=['float']).columns
        for col in cols:
            df[col] = df[col].str.replace(',','.')
        df[cols] = df[cols].apply(pd.to_numeric, downcast='float', errors='coerce')

        columns=df.columns
        mean=[df[column].mean() for column in columns]
        mean_list.append(mean)


        
new_df=pd.DataFrame(mean_list,index=index,columns=columns)

new_df.to_excel('output.xlsx')

