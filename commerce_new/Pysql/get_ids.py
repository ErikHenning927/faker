import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connections.all_connections import postgres_local
from utils.utils import load_sql

get_sales_channel_ids = load_sql('getids/get_sales_channel_ids.sql', 'Queries')
get_customer_ids = load_sql('getids/get_customersids.sql', 'Queries')
get_address_ids = load_sql('getids/get_address_ids.sql', 'Queries')
get_paymentids = load_sql('getids/get_paymentids.sql', 'Queries')
get_paymentsmodes = load_sql('getids/get_paymentsmodes.sql', 'Queries')

def execute_query(query):
    conn = postgres_local()
    if conn is None:
        print("Conexão não realizada.")
        return []
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows


# results = execute_query(get_paymentsmodes)
# all_results = [r[0] for r in results]
# print(all_results)