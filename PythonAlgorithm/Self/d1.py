import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('data_download.csv')
filteredDF_Input = df[(df.date == "01/17/2023")]
compareDF_Input = df[(df.date == "01/18/2023")]
filteredDF_Input = filteredDF_Input.drop(columns=["symbol", "exchange", "date", "adjusted close", "stock price for iv", "*"])
compareDF_Input = compareDF_Input.drop(columns=["symbol", "exchange", "date", "adjusted close", "stock price for iv", "*"])
print(filteredDF_Input.isnull().sum())
X = filteredDF_Input['volume']
y = filteredDF_Input.drop(columns=['volume'])
print(filteredDF_Input.ask)
#print(filteredDF_Input.ask.values)


# np.random.seed(42)
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2. random_state=101)
# clf = RandomForestClassifier(n_estimators=100)
# clf.fit(X_train, y_train)
#
# clf.score(X_test, y_test)

# dataplot = sb.heatmap(filteredDF_Input.corr(), cmap="YlGnBu", annot=True)
# plt.show()
#
# print(volumeDF.head())
# print(restDF.head())

