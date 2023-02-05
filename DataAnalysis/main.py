import pandas as pd

df = pd.read_csv('C:/Users/prabh/PycharmProjects/AI_ML/DataAnalysis/COVID-19_Report.csv')

# Finding Maximum number
maxValue = df.critical_staffing_shortage_today_no.max()
print("The maximum value for critical_staffing_shortage_today_no is: ", maxValue)

# Finding Minimum number
minValue = df.critical_staffing_shortage_today_no.min()
print("The minimum value for critical_staffing_shortage_today_no is: ", minValue)

# Finding Mode number
modeValue = df.critical_staffing_shortage_today_no.mode()
print("The mode value for critical_staffing_shortage_today_no is: ", modeValue)
