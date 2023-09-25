#Importer library
import pandas as pd
import seaborn  as sb
import matplotlib.pyplot as plt
import numpy as np

from seaborn.utils import get_dataset_names


flight=sb.load_dataset('flights')
print("********using dataset flights********")
flight.columns
print(f"flight.columns = {flight.columns}")
flight.head()
print(f"flight.head() = {flight.head()}")
flight.info()
print(f"flight.info() = {flight.info()}")
flight.shape
print(f"flight.shape = {flight.shape}")
flight.describe()
print(f"flight.describe() = {flight.describe()}")
 
cat_columns = flight.select_dtypes('O').columns
num_columns = flight.select_dtypes('int').columns

print(f"cat_columns = {cat_columns}")
print(f"num_columns = {num_columns}")
