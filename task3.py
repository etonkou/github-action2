import pandas as pd

data = pd.read_csv("food-consumption.csv")
data.head()
data.shape
data.info()
data.describe()
data.corr()

from pandas_profiling import ProfileReport
profile = ProfileReport(data, title="Pandas Profiling Report", explorative=True)
profile.to_file('./reports/report.html')