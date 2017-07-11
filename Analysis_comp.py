import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

df = pd.read_csv('E:\Project\Company-Registration\company_2015_KAR.csv')
# print(df.head())


## Viz1: Comparitive analysis of Number of companies established in a given year

df.columns = ['Corporate_ID','RegYear','CompanyName',
'Status','Type','Category','Capital','PaidUpCapital','State','Registrar','Domain','Address','SubCategory']


#obtaining year from 'date of registration':

df['RegYear'] = pd.to_datetime(df['RegYear']).dt.year

dfYear= pd.DataFrame(df.groupby('RegYear')['Corporate_ID'].count())
dfYear.plot(kind='bar')
plt.show()
