import pandas as pd
from sqlalchemy import create_engine


USER = 'ironhacker_read'
PASSWORD = 'ir0nhack3r'
HOST = '35.239.232.23'


def get_data_from_file(file_type, path):
    if file_type == 'csv':
        return pd.read_csv(path)
    if file_type == 'json':
        return pd.read_json(path)

def get_data_from_db(database, table, user=USER, password=PASSWORD, host=HOST):
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
    query = f'SELECT * FROM {table}'
    data = pd.read_sql(query, engine)
    return data

def get_data(way, file_type=None, file_path=None, database=None, table=None, user=USER,
             password=PASSWORD, host=HOST):
    if way == 'file':
        return get_data_from_file(file_type, file_path)
    if way == 'database':
        return get_data_from_db(database, table, user, password, host)

def write_on_database(database_name, db_table, dataframe, user=USER, password=PASSWORD,
                      host=HOST, index=False):
    conn_string = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
    engine = create_engine(conn_string)
    dataframe.to_sql(name=db_table, con=engine, index=index, if_exists='append')

def write_in_file(dataframe, title='myFile'):
    dataframe.to_csv(f'{title}.csv')

def write_data(dataframe, way, database_name=None, db_table=None, user=USER, password=PASSWORD,
               host=HOST, file_title=None, index=True):
    if way == 'file':
        return write_in_file(dataframe, file_title)
    if way == 'database':
        return write_on_database(database_name, db_table, dataframe, user, password, host, index)