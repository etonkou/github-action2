import pandas as pd

data = pd.read_csv("food-consumption.csv")
data.head()
data.shape
data.info()
data.describe()
num_columns = data.select_dtypes('int').columns
data=data[num_columns]
data.corr()

from pandas_profiling import ProfileReport
profile = ProfileReport(data, title="Pandas Profiling Report", explorative=True)
profile.to_file('./reports/report.html')
