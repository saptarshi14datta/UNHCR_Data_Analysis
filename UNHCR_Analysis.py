#Name: UNHCR_Analysis
#Preparer: Saptarshi Datta
#Date: Nov 3, 2019
#Data Source: http://popstats.unhcr.org/en/asylum_seekers_monthly
import pandas as pd
import numpy as np
from scipy.stats import stats
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt

from matplotlib.pyplot import pie, axis, show
from datetime import datetime

excel_file_path = (r'C:\Users\b0589940\Documents\Python Scripts\UNHCR_Data_Analysis-master\UNHCR_Data_Analysis-master\unhcr_popstats_export_asylum_seekers_monthly.csv')

data = pd.read_csv(excel_file_path,sep=',',skiprows=3)
data['Value'] = data['Value'].replace('*', np.nan)
data.dropna(subset = ['Value'],axis=0,  how='any', inplace=True)


#How has the number of asylum applications varied over the years

#Change variable type for groupby
data['Year']= data['Year'].astype(str) 
data['Value']= data['Value'].astype(int) 
data['Country / territory of asylum/residence']= data['Country / territory of asylum/residence'].astype(str) 
data['Origin']= data['Origin'].astype(str) 
data['Month']= data['Month'].astype(str) 
'''
asylum_year = data.groupby(by=['Year'])['Value'].sum()
data_year = pd.DataFrame({'Year':asylum_year.index, 'Asylum Applications':asylum_year.values})

sns.set(style="white")
sns.set_context("paper")
asylum_year_plot = sns.barplot(x='Year',y='Asylum Applications', data=data_year, palette=("Blues_d"))
asylum_year_plot.set_xticklabels(asylum_year_plot.get_xticklabels(), rotation=90)
asylum_year_plot.set_title('Asylum Applications by year')


#How has the number of asylum applications varied by country of origin - top 10
origin_country = data.groupby(by=['Origin'])['Value'].sum()
data_origin_country = pd.DataFrame({'Country of Origin':origin_country.index, 'Asylum Applications':origin_country.values})
data_origin_country = data_origin_country.sort_values(by=['Asylum Applications'], ascending=False)
data_origin_country.reset_index(inplace=True, drop=True)

#sns.set(style="white", context="talk")
sns.set_context("paper")
origin_country_plot = sns.barplot(x='Country of Origin',y='Asylum Applications', data=data_origin_country, palette=("Blues_d"), order=data_origin_country.iloc[0:9,0])
origin_country_plot.set_xticklabels(origin_country_plot.get_xticklabels(), rotation=90)
origin_country_plot.set_title('Top 10 Countries from where Asylum Seekers Originated')

#Where are asylum seekers seeking asylum - top 10
asylum_country = data.groupby(by=['Country / territory of asylum/residence'])['Value'].sum()
data_asylum_country = pd.DataFrame({'Country of Asylum':asylum_country.index, 'Asylum Applications':asylum_country.values})
data_asylum_country = data_asylum_country.sort_values(by=['Asylum Applications'], ascending=False)
data_asylum_country.reset_index(inplace=True, drop=True)

sns.set_context("paper")
asylum_country_plot = sns.barplot(x='Country of Asylum',y='Asylum Applications', data=data_asylum_country, palette=("Blues_d"), order=data_asylum_country.iloc[0:9,0])
asylum_country_plot.set_xticklabels(asylum_country_plot.get_xticklabels(), rotation=90)
asylum_country_plot.set_title('Top 10 Countries that provided Asylum')

#In 2016 which countries produced the highest number of asylum seekers

year_mask = (data['Year']=='2016')
data_set_year = data.loc[year_mask]

origin_country_year = data_set_year.groupby(by=['Origin'])['Value'].sum()
data_origin_country_year = pd.DataFrame({'Country of Origin':origin_country_year.index, 'Asylum Applications':origin_country_year.values})
data_origin_country_year = data_origin_country_year.sort_values(by=['Asylum Applications'], ascending=False)
data_origin_country_year.reset_index(inplace=True, drop=True)

#sns.set(style="white", context="talk")
sns.set_context("paper")
origin_country_year_plot = sns.barplot(x='Country of Origin',y='Asylum Applications', data=data_origin_country_year, palette=("Blues_d"), order=data_origin_country_year.iloc[0:9,0])
origin_country_year_plot.set_xticklabels(origin_country_year_plot.get_xticklabels(), rotation=90)
origin_country_year_plot.set_title('Top 10 Origin Countries of Asylum Seekers in 2016')

#Which countries have asylum seekers from Syria seeked asylum in 2016
country_year_mask = (data['Year']=='2016') & (data['Origin']=='Syrian Arab Rep.')
data_set_country_year = data.loc[country_year_mask]

asylum_country_syria = data_set_country_year.groupby(by=['Country / territory of asylum/residence'])['Value'].sum()
data_asylum_country_syria = pd.DataFrame({'Country of Asylum':asylum_country_syria.index, 'Asylum Applications':asylum_country_syria.values})
data_asylum_country_syria = data_asylum_country_syria.sort_values(by=['Asylum Applications'], ascending=False)
data_asylum_country_syria.reset_index(inplace=True, drop=True)

sns.set_context("paper")
asylum_country_syria_plot = sns.barplot(x='Country of Asylum',y='Asylum Applications', data=data_asylum_country_syria, palette=("Blues_d"), order=data_asylum_country_syria.iloc[0:9,0])
asylum_country_syria_plot.set_xticklabels(asylum_country_syria_plot.get_xticklabels(), rotation=90)
asylum_country_syria_plot.set_title('Countries providing shelter to Syrian Asylum Seekers in 2016')


#Which countries have asylum seekers from China seeked asylum in 2016
country_year_mask = (data['Year']=='2016') & (data['Origin']=='China')
data_set_country_year = data.loc[country_year_mask]

asylum_country_china = data_set_country_year.groupby(by=['Country / territory of asylum/residence'])['Value'].sum()
data_asylum_country_china = pd.DataFrame({'Country of Asylum':asylum_country_china.index, 'Asylum Applications':asylum_country_china.values})
data_asylum_country_china = data_asylum_country_china.sort_values(by=['Asylum Applications'], ascending=False)
data_asylum_country_china.reset_index(inplace=True, drop=True)

sns.set_context("paper")
asylum_country_china_plot = sns.barplot(x='Country of Asylum',y='Asylum Applications', data=data_asylum_country_china, palette=("Blues_d"), order=data_asylum_country_china.iloc[0:9,0])
asylum_country_china_plot.set_xticklabels(asylum_country_china_plot.get_xticklabels(), rotation=90)
asylum_country_china_plot.set_title('Countries providing shelter to Chinese Asylum Seekers in 2016')
'''
#German asylum seekers by country of origin in 2016
asylum_country_year_mask = (data['Year']=='2016') & (data['Country / territory of asylum/residence']=='Germany')
data_set_asylum_country_year = data.loc[asylum_country_year_mask ]

germany_asylum_country_year = data_set_asylum_country_year.groupby(by=['Origin'])['Value'].sum()
data_germany_asylum_country = pd.DataFrame({'Country of Origin':germany_asylum_country_year.index, 'Asylum Applications':germany_asylum_country_year.values})
data_germany_asylum_country = data_germany_asylum_country.sort_values(by=['Asylum Applications'], ascending=False)
data_germany_asylum_country.reset_index(inplace=True, drop=True)

plt.pie(data_germany_asylum_country['Asylum Applications'][:5], labels=data_germany_asylum_country['Country of Origin'][:5],autopct='%1.1f%%');
plt.title('Top 5 Nationalities seeking asylum in Germany in 2016')
plt.tight_layout()
plt.axis('equal')
plt.show()


print("Done")