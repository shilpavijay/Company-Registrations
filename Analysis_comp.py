import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('E:\Project\Company-Registration\company_master_2015_Karnataka.csv')
# print(df.head())


## Viz1: Comparitive analysis of Number of companies established in a given year

df.columns = ['Corporate_ID','RegYear','CompanyName',
'Status','Type','Category','Capital','PaidUpCapital','State','Registrar','Domain','Address','SubCategory']


#obtaining year from 'date of registration':

df['RegYear']=pd.to_datetime(df['RegYear'])
df['RegYear'].dt.year
print(df['RegYear'].dt.year.head())

plt.scatter(df.groupby['RegYear'], df.groupby['RegYear'].count())
plt.show() 


