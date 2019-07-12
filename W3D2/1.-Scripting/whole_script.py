import pandas as pd
import datetime as dt


data = pd.read_csv('data/sales_01.04.2015.csv')

# Cleaning
data = data.drop('Unnamed: 0', axis = 1)
data['date'] = pd.to_datetime(data['date'])

#Create the aggregates
by_shop = data.groupby('shop_id').sum()
by_shop = by_shop.drop(['item_id'], axis = 1)
by_shop = by_shop.rename(columns = {'item_price': 'shop_earnings', 'item_cnt_day': 'total_items_sold'})
by_shop['date'] = dt.datetime.today().strftime("%m/%d/%Y")

by_item = data.groupby('item_id').sum().drop(['shop_id'], axis = 1)
by_item = by_item.rename(columns = {'item_price': 'item_earnings', 'item_cnt_day': 'total_items_sold'})
by_item['date'] = dt.datetime.today().strftime("%m/%d/%Y")

# Write into the db
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://ironhacker_read:ir0nhack3r@35.239.232.23/retail_sales')

data.to_sql('raw_sales', engine, if_exists= 'append', index = False)
by_item.to_sql('sales_by_item', engine, if_exists='append')
by_shop.to_sql('sales_by_shop', engine, if_exists='append')
