import pandas as pd
import matplotlib.pyplot as plt
# #df = pd.read_csv('COVID-19_Report.csv', nrows=2, parse_dates=['date'], usecols=['date', 'state'])
#df = pd.read_csv('COVID-19_Report.csv', nrows=2, usecols=['date', 'state'])
#print(df.columns)
# df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d') # same as parse_dates
# print(df)
# year = df.date.dt.year
# print(year)
#
# Data Cleaning
# 	1. Value Range
# 	2. Distribution checking
# 	4. Missing value
# 	5. Correlation of data
df = pd.read_csv('COVID-19_Report.csv', usecols=['critical_staffing_shortage_today_yes'])
print(df.min())
print(df.max())
print(df.mean())
mode = df['critical_staffing_shortage_today_yes'].mode()[0]
print(mode)

# Get the histogram
hist = df.hist(bins=10)
print(df.describe())
# Show the histogram
plt.show()
