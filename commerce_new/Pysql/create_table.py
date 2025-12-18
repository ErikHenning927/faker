import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connections.all_connections import postgres_local
from utils.utils import load_sql

def execute_query_create(query):
    conn = postgres_local()
    if conn is None:
        print("Conexão não realizada.")
        return []
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()


tables = [
    ("dim_courier", load_sql('dim_courier.sql', 'Table_postgres')),
    ("dim_payment_mode", load_sql('dim_paymentModes.sql', 'Table_postgres')),
    ("dim_productBrand", load_sql('dim_productBrand.sql', 'Table_postgres')),
    ("dim_productFamily", load_sql('dim_productFamily.sql', 'Table_postgres')),
    ("dim_productLine", load_sql('dim_productLine.sql', 'Table_postgres')),
    ("dim_salesChannel", load_sql('dim_salesChannel.sql', 'Table_postgres')),
    ("dim_variantProduct", load_sql('dim_variantProduct.sql', 'Table_postgres')),
    ("dim_warehouse", load_sql('dim_warehouse.sql', 'Table_postgres')),
    ("addresses", load_sql('addresses.sql', 'Table_postgres')),
    ("cartEntry", load_sql('cartEntry.sql', 'Table_postgres')),
    ("paymentInfo", load_sql('paymentInfo.sql', 'Table_postgres')),
    ("customerData", load_sql('customerData.sql', 'Table_postgres')),
    ("orders", load_sql('orders.sql', 'Table_postgres')),
    ("invoice", load_sql('invoice.sql', 'Table_postgres')),
]

for name, query in tables:
    print(f"Criando tabela: {name}")
    execute_query_create(query)
