import pandas as pd

data = pd.read_csv("food-consumption.csv")
data.head()
data.shape
data.info()
data.describe()
#num_columns = data.select_dtypes('int').columns
#data=data[num_columns]
data=data.drop('Country',axis=1)
data.corr()

print("***********")
print(f"data.shape: {data.shape}")
print(f"data.info(): {data.info()}")
print(f"{data.head()}")
from pandas_profiling import ProfileReport
profile = ProfileReport(data, title="Pandas Profiling Report", explorative=True)
profile.to_file('report.html')
