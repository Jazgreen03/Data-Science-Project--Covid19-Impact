# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 01:05:36 2024

@author: jazmi
"""
import pandas as pd
import numpy as n
import matplotlib.pyplot as plt

file_path = r"C:\Users\jazmi\OneDrive\Documents\Data Analytics Notes\Covid19Data.csv"
data = pd.read_csv(file_path)

data = data.dropna()
x = data.iloc[:, 4].values  # 5th column (index 4)
y = data.iloc[:, 8].values  # 9th column (index 8)
print(data.head())

plt.figure(figsize=(9,7))
plt.plot(x, y, color='red', marker='o', linestyle='-', label='Line Graph')
plt.xlabel("Total Death", fontsize=13, fontweight='bold')
plt.ylabel("GDP Per Capita", fontsize=13, fontweight='bold')
plt.title("Line Graph Example", fontsize = 16)
plt.legend()
plt.grid(True)
plt.show
