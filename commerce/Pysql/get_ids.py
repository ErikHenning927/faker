import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connections.all_connections import db_local
from utils.utils import load_sql

def get_payments_modes_to_process():
    conn = db_local()
    if conn is None:
        print("Conexão não realizada.")
        return
    cursor = conn.cursor()
    query = load_sql('getids/get_paymentsmodes.sql', 'Queries')
    cursor.execute(query)
    rows = cursor.fetchall()
    all_results = []
    for row in rows:
        vtex_order_id = row[0]
        all_results.append(vtex_order_id)
    conn.close()
    return all_results

def get_payments_ids_to_process():
    conn = db_local()
    if conn is None:
        print("Conexão não realizada.")
        return
    cursor = conn.cursor()
    query = load_sql('getids/get_paymentids.sql', 'Queries')
    cursor.execute(query)
    rows = cursor.fetchall()
    all_results = []
    for row in rows:
        vtex_order_id = row[0]
        all_results.append(vtex_order_id)
    conn.close()
    return all_results

def get_address_ids_to_process():
    conn = db_local()
    if conn is None:
        print("Conexão não realizada.")
        return
    cursor = conn.cursor()
    query = load_sql('getids/get_address_ids.sql', 'Queries')
    cursor.execute(query)
    rows = cursor.fetchall()
    all_results = []
    for row in rows:
        vtex_order_id = row[0]
        all_results.append(vtex_order_id)
    conn.close()
    return all_results

def get_customer_ids_to_process():
    conn = db_local()
    if conn is None:
        print("Conexão não realizada.")
        return
    cursor = conn.cursor()
    query = load_sql('getids/get_customersids.sql', 'Queries')
    cursor.execute(query)
    rows = cursor.fetchall()
    all_results = []
    for row in rows:
        vtex_order_id = row[0]
        all_results.append(vtex_order_id)
    conn.close()
    return all_results

def get_sales_channel_ids_to_process():
    conn = db_local()
    if conn is None:
        print("Conexão não realizada.")
        return
    cursor = conn.cursor()
    query = load_sql('getids/get_sales_channel_ids.sql', 'Queries')
    cursor.execute(query)
    rows = cursor.fetchall()
    all_results = []
    for row in rows:
        vtex_order_id = row[0]
        all_results.append(vtex_order_id)
    conn.close()
    return all_results
