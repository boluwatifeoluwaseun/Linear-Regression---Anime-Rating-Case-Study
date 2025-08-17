# Import necessary libraries for data manipulation
import numpy as np
import pandas as pd

# Import libraries to help with data visualisation
import matplotlib.pyplot as plt
import seaborn as sns

# Apply Seaborn's default style settings to make Matplotlib plots look nicer (better colors, grid, fonts, etc.)
sns.set()

# Pandas display settings (optional, only affects how DataFrames are shown) 
pd.set_option("display.max_columns", None)  # Show all columns when printing a DataFrame
pd.set_option("display.max_rows", 200)      # Show up to 200 rows when printing a DataFrame

# Splits dataset into training and testing sets
from sklearn.model_selection import train_test_split  

# Used to build a linear regression model
from sklearn.linear_model import LinearRegression     

# Model evaluation metrics to check model performance
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score