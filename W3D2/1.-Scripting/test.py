import pandas as pd
import data_cleaning as dc
import aggregates_creation_new as acn

data = pd.read_csv('data/sales_01.04.2015.csv')

data = dc.clean_sales_data(sales_dataframe=data)

by_shop, by_item = acn.create_agg(data=data)

# NEEDS TO BE BUILT
write_into_db(by, shop, by_item, data)