# Name: PRABHJEET SINGH
# ID: C0885089

import pandas as pd

# Importing file with selected columns
df = pd.read_csv('COVID-19_Report.csv',
                 usecols=['hospital_onset_covid_coverage', 'critical_staffing_shortage_today_not_reported',
                          'total_staffed_pediatric_icu_beds'])


# Function to print min, max, mean and mode values
def print_values(columnName):
    print(columnName, "Min value is : ", df[columnName].min())  # Minimum value from column
    print(columnName, "Max value is : ", df[columnName].max())  # Maximum value from column
    print(columnName, "Mean value is : ", df[columnName].mean())  # Mean value of column
    print(columnName, "Mode value is : ", df[columnName].mode()[0])  # Mode value of column
    print('\n')


# Calling the print_values function
print_values('hospital_onset_covid_coverage')
print_values('critical_staffing_shortage_today_not_reported')
print_values('total_staffed_pediatric_icu_beds')
