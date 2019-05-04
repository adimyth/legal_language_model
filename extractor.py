from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv
import os
import pandas as pd
import random

load_dotenv('.env')

user = os.environ.get('user')
password = os.environ.get('password')
dbname = os.environ.get('dbname')
host = os.environ.get('host')
port = os.environ.get('port')

db_string = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'


def load_data(query, filename):
    try:
        engine = create_engine(db_string, poolclass=NullPool)
        data = pd.read_sql(query, con=engine)
        data.to_csv(filename, index=False)
        engine.dispose()
    except Exception as e:
        print(f'Exception: {e}')


if __name__ == '__main__':
    load_data('SELECT text FROM justiceleague LIMIT 10000', 'judgements.csv')
