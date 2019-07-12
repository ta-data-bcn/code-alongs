import pandas as pd

def clean_sales_data(sales_dataframe):
    sales_dataframe = sales_dataframe.drop('Unnamed: 0', axis=1)
    sales_dataframe['date'] = pd.to_datetime(sales_dataframe['date'])
    return sales_dataframe

