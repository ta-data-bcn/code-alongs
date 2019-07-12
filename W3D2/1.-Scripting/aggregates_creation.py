import datetime as dt


def create_sales_aggregate(dataframe, column_group, column_drop_list, new_names_columns):
    agg_dataframe = dataframe.groupby(column_group).sum().drop(column_drop_list, axis=1)
    agg_dataframe = agg_dataframe.rename(columns=new_names_columns)
    agg_dataframe['date'] = dt.datetime.today().strftime("%m/%d/%Y")
    return agg_dataframe