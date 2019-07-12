import impexp as ie
import data_cleaning as dclean
import aggregates_creation as agg

TODAYS_FILE = 'data/sales_01.04.2015.csv'
DATABASE_NAME = 'retail_sales'

todays_data = ie.get_data(way='file', file_type='csv', file_path=TODAYS_FILE)

todays_data = dclean.clean_sales_data(todays_data)

agg_by_shop = agg.create_sales_aggregate(todays_data, column_group='shop_id', column_drop_list=['item_id'],
                                 new_names_columns={'item_price': 'shop_earnings', 'item_cnt_day': 'total_items_sold'})
agg_by_item = agg.create_sales_aggregate(todays_data, column_group='item_id', column_drop_list=['shop_id'],
                                 new_names_columns={'item_price': 'item_earnings', 'item_cnt_day': 'total_items_sold'})

ie.write_data(dataframe=todays_data, way='database', db_table='raw_sales', database_name=DATABASE_NAME, index=False)
ie.write_data(dataframe=agg_by_shop, way='database', db_table='sales_by_shop', database_name=DATABASE_NAME)
ie.write_data(dataframe=agg_by_item, way='database', db_table='sales_by_item', database_name=DATABASE_NAME)



