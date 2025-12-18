import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connections.all_connections import *
from utils.utils import load_sql, chunked_iterable

def insert_customer_info_to_db(all_orderCustomers):
    conn = postgres_local()
    cursor = conn.cursor()

    insert_query = load_sql('customer/insert_orderCustomer.sql', 'Queries')
    update_query = load_sql('customer/update_orderCustomer.sql', 'Queries')
    check_query = load_sql('customer/check_orderCustomer.sql', 'Queries')

    cursor.execute(check_query)
    existing_ids = set((row[0], ) for row in cursor.fetchall())

    for chunk in chunked_iterable(all_orderCustomers, 10000): 
        insert_batch = []
        update_batch = []
        for customer in chunk:
            try:
                key = customer['customerId']
                if key not in existing_ids:
                    customer_values = (
                        customer['customerId'],
                        customer.get('customerDocument', None),
                        customer.get('customerFirstName', None),
                        customer.get('customerLastName', None),
                        customer.get('customerDocumentType', None),
                        customer.get('customerPhone', None),
                        customer.get('customerEmail', None),
                        customer.get('customerTradeName', None),
                        customer.get('customerCorporateDocument', None),
                        customer.get('customerStateInscription', None),
                        customer.get('customerCorporatePhone', None),
                        customer.get('customerIsCorporate', None),
                        customer.get('customerUserProfileId', None),
                        customer.get('customerUserProfileVersion', None),
                        customer.get('customerClass', None),
                        customer.get('customerCode', None)
                        )
                    insert_batch.append(customer_values)
                    existing_ids.add(key)
                else:
                    update_values = (

                        customer.get('customerDocument', None),
                        customer.get('customerFirstName', None),
                        customer.get('customerLastName', None),
                        customer.get('customerDocumentType', None),
                        customer.get('customerPhone', None),
                        customer.get('customerEmail', None),
                        customer.get('customerTradeName', None),
                        customer.get('customerCorporateDocument', None),
                        customer.get('customerStateInscription', None),
                        customer.get('customerCorporatePhone', None),
                        customer.get('customerIsCorporate', None),
                        customer.get('customerUserProfileId', None),
                        customer.get('customerUserProfileVersion', None),
                        customer.get('customerClass', None),
                        customer.get('customerCode', None),
                        customer['customerId']
                        )
                    update_batch.append(update_values)
            except KeyError as e:
                print(f"Missing key {e} in key: {key}")

        if insert_batch:
            try:
                cursor.executemany(insert_query, insert_batch)
                print(f"{len(insert_batch)} clientes inseridos no banco com sucesso.")
            except Exception as e:
                print(f"Erro de integridade ao inserir lote. Tentando linha por linha... {e}")
                success_count = 0
                for row in insert_batch:
                    try:
                        cursor.execute(insert_query, row)
                        success_count += 1
                    except Exception as e:
                        print(f"Ignorado: {e}")
                print(f"{success_count} clientes inseridos com sucesso após tratamento de erros.")
        if update_batch:
            cursor.executemany(update_query, update_batch)
            print(f"{len(update_batch)} clientes atualizados no banco com sucesso.")

    conn.commit()
    cursor.close()
    conn.close()