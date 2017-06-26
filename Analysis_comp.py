import pandas as pd

df = pd.read_csv('E:\Project\Company-Registration\company_master_2015_Karnataka.csv')
# print(df.head())


## Viz1: Comparitive analysis of Number of companies established in a given year



#obtaining year from 'date of registration':

df['DATE_OF_REGISTRATION']=pd.to_datetime(df['DATE_OF_REGISTRATION'])
df['DATE_OF_REGISTRATION'].dt.year
print(df['DATE_OF_REGISTRATION'].dt.year.head())

