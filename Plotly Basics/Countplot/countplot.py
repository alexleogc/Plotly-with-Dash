import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go 

df = pd.read_csv('data/mocksurvey.csv')

df.set_index(df.columns[0],inplace=True)

#print(df,df.index,df.columns)

for i in df.index:

    data = [go.Bar(x=df.index, y=df.loc[i][j],name=j) for j in df.columns]

print(data)

#print(df.loc[df.index[1]][df.columns[0]])