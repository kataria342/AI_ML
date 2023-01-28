import pandas as pd
import matplotlib
from IPython.display import display



df = pd.read_csv("kdrama.csv", sep=",")
print(df.shape)
display(df)