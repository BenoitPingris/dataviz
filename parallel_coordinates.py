import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import parallel_coordinates
from sklearn import preprocessing

cols = ['MPG', 'Cylinders', 'Displacement',
        'Horsepower', 'Weight', 'Acceleration', 'Origin']
data = pd.read_csv('data.csv', sep=',', usecols=cols)

min_max_scaler = preprocessing.MinMaxScaler()

# normalize the data between 0 & 1
for col in data.columns:
    if col == 'Origin':
        continue
    x = data[[col]].values.astype(float)
    x_scaled = min_max_scaler.fit_transform(x)
    data[[col]] = x_scaled

parallel_coordinates(data, 'Origin', color=['#556270', 'blue', '#C7F464'])
plt.show()
