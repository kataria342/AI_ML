import pandas as pd
df = pd.read_csv("COVID-19_Report.csv")


# Explore Head df.head()
print(df.head())

# Explore column data
#print(df['state'])

# Explore all the columns
#print(df.columns)
totalCount = df.critical_staffing_shortage_today_no.count()
maxValue = df.critical_staffing_shortage_today_no.max()
minValue = df.critical_staffing_shortage_today_no.min()
modeValue = df.critical_staffing_shortage_today_no.mode()

print("Total Count is :", totalCount)
print("Max value is :", maxValue)
print("Min value is :", minValue)
print("Mode value is :", modeValue)
"""
# Maximum, minimum, and mode of critical Staffing Shortage today
print("Maximum Value", df['critical_staffing_shortage_today_no'].max())
print("Minimum Value", df['critical_staffing_shortage_today_no'].min())
print("Mode value", df['critical_staffing_shortage_today_no'].mode())
"""