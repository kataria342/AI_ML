import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

import seaborn as sb
from sklearn.preprocessing import LabelEncoder, StandardScaler

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["Date", "Data"]
data = pd.read_csv("data_download1.csv")
trainData = data[['expiratdataion'] == '01/17/2023']
#print(trainData.columns)
X = trainData[['ask', 'bid', 'open interest']].values
Y = trainData[['strike']].values
label_encoder = LabelEncoder()
Y = label_encoder.fit_transform(Y)
X = StandardScaler().fit_transform(X)
plt.plot(X,Y)
plt.show()

#plt.plot(trainData.strike, trainData.expiration, color='green')
#plt.plot(trainData['mean price'], trainData.expiration, color='red')
#plt.plot(trainData['open interest'],trainData.expiration, color='blue')
#plt.plot(trainData['ask'], trainData.expiration, color='yellow')
#plt.plot(trainData['bid'],trainData.expiration, color='black')
#dataplot = sb.heatmap(trainData.corr(), cmap="YlGnBu", annot=True)
#plt.show()
#plt.plot(trainData['volume'], trainData.expiration, color='orange', label='Volume')
#plt.show()
# print(trainData.head())
