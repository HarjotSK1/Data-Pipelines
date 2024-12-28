import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
def readcsv(file):
    return pd.read_csv(file)

sales_data_df = readcsv('sales_data.csv')

def data_cleaning(df):

    # Drop rows with missing values and create new dataframe of just missing value rows
    df_cleaned = df.dropna()
    df_missing = df[~df.index.isin(df_cleaned.index)]

    # Convert columns to appropriate data types
    df_cleaned['date'] = pd.to_datetime(df_cleaned['date'])
    df_cleaned['price'] = pd.to_numeric(df_cleaned['price'])
    df_cleaned['quantity'] = pd.to_numeric(df_cleaned['quantity'])
    df_cleaned['customer_id'] = df_cleaned['customer_id'].astype('int')
    df_cleaned['product_id'] = df_cleaned['product_id'].astype('int')
    df_cleaned['transaction_id'] = df_cleaned['transaction_id'].astype('int')

    # Drop duplicate rows
    df_cleaned.drop_duplicates(inplace=True)

    return df_cleaned, df_missing

sales_data_cleaned, sales_data_missing = data_cleaning(sales_data_df)

# ADD COLUMNS TO THE DATAFRAME

# add total sales column to the dataframe
sales_data_cleaned['total_sales'] = sales_data_cleaned['price'] * sales_data_cleaned['quantity']
# add day of the week column to the dataframe
sales_data_cleaned['day_of_week'] = sales_data_cleaned['date'].dt.day_name()
# add month column to the dataframe
sales_data_cleaned['month'] = sales_data_cleaned['date'].dt.month_name()
# add column for the quarter of the year
sales_data_cleaned['quarter'] = sales_data_cleaned['date'].dt.quarter
# add column for cumulative sales
sales_data_cleaned['cumulative_sales'] = sales_data_cleaned['total_sales'].cumsum()
# add column for cumulative sales percentage
sales_data_cleaned['cumulative_sales_percentage'] = sales_data_cleaned['cumulative_sales'] / sales_data_cleaned['total_sales'].sum()
# add repeat customer column
sales_data_cleaned['repeat_customer'] = sales_data_cleaned['customer_id'].duplicated()
sales_data_cleaned.head(), sales_data_cleaned.size, sales_data_cleaned.isna().sum()