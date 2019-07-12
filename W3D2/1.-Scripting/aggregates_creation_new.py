import datetime as dt

def create_agg(data):
    by_shop = data.groupby('shop_id').sum()
    by_shop = by_shop.drop(['item_id'], axis = 1)
    by_shop = by_shop.rename(columns={'item_price': 'shop_earnings', 'item_cnt_day': 'total_items_sold'})
    by_shop['date'] = dt.datetime.today().strftime("%m/%d/%Y")

    by_item = data.groupby('item_id').sum().drop(['shop_id'], axis = 1)
    by_item = by_item.rename(columns = {'item_price': 'item_earnings', 'item_cnt_day': 'total_items_sold'})
    by_item['date'] = dt.datetime.today().strftime("%m/%d/%Y")
    return by_shop, by_item
