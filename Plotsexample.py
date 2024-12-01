# -*- coding: utf-8 -*
"""
Created on Thu Nov 28 01:05:36 2024

@author: jazmi
"""
import pandas as pd
import numpy as n
import seaborn as sns
import matplotlib.pyplot as plt

file_path = r"C:\Users\jazmi\OneDrive\Documents\Data Analytics Notes\Covid19Data.csv"
data = pd.read_csv(file_path)
specific_country_code = ['United States', 'Canada']
country_code_two = 'Canada'
country_code_three = 'Australia'

filtered_data = data.loc[data['COUNTRY'].isin(specific_country_code)]
print(filtered_data.head())

data = data.dropna()
x = data.iloc[:, 4].values  
y = data.iloc[:, 8].values 
a = data['Total_Cases'] 
b = data['GDP_Per_Capita']  

print(data.head())
country_cases = data.groupby('COUNTRY')['Total_Cases'].sum().sort_values(ascending=False)
top_10 = country_cases.head(10)
top_3 = country_cases.head(3).index
plt.figure(figsize=(12, 8))
top_10.plot(kind='bar', color='lightblue', edgecolor='black')
plt.title('Top 10 Countries with Highest Total Cases', fontsize=16)
plt.xlabel('Country', fontsize=14, fontweight='bold')
plt.ylabel('Total Cases', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig(r"C:\Users\jazmi\OneDrive\Documents\Data Analytics Notes\Top_10_Countries_Total_Cases.png")
plt.show()

data['DATE'] = pd.to_datetime(data['DATE'])
top_3_data = data[data['COUNTRY'].isin(top_3)]

plt.figure(figsize=(12, 8))
for country in top_3:
    country_data = top_3_data[top_3_data['COUNTRY'] == country]
    plt.plot(
        country_data['DATE'], 
        country_data['GDP_Per_Capita'], 
        label=country
    )


# Customize the plot
plt.xlabel('Date', fontsize=14, fontweight='bold')
plt.ylabel('GDP per Capita', fontsize=14, fontweight='bold')
plt.title('GDP per Capita Trends Over Time (Top 3 Countries)', fontsize=16)
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 8))
for country in top_3:
    country_data = top_3_data[top_3_data['COUNTRY'] == country]
    plt.plot(country_data['DATE'], country_data['Stringency_Index'], label=country, linewidth=2)

plt.title('Stringency Index Over Time (Top 3 Countries)', fontsize=13)
plt.xlabel('Date', fontsize=15, fontweight='bold')
plt.ylabel('Stringency Index', fontsize=14, fontweight='bold')
plt.legend(title="Country")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"C:\Users\jazmi\OneDrive\Documents\Data Analytics Notes\Top_3_Total_Cases.png")
plt.show()

plt.figure(figsize=(9, 7))
plt.scatter(a, b, color='blue', alpha=0.7, s=30, edgecolor='green', label='Data Points')
plt.xlabel("Total Cases", fontsize=13, fontweight='bold')  # Replace with actual label
plt.ylabel("GDP per Capita", fontsize=13, fontweight='bold')  # Replace with actual label
plt.title("Total Death vs GDP per Capital", fontsize=16)
plt.legend()
plt.grid(True)
plt.savefig(r"C:\Users\jazmi\OneDrive\Documents\Data Analytics Notes\Top_Deaths_GDP.png")
plt.show()

sns.regplot(x='Stringency_Index', y='GDP_Per_Capita', data=data, line_kws={'color': 'red'}, scatter_kws={'s': 15})

plt.title('Regression of GDP Per Capita on Stringency Index')
plt.xlabel('Stringency Index')
plt.ylabel('GDP Per Capita')
plt.show()
