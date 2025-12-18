import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connections.all_connections import *
from utils.utils import load_sql, chunked_iterable

def insert_address_to_db(all_addresses):
    conn = postgres_local()
    cursor = conn.cursor()

    insert_query = load_sql('addresses/insert_addresses.sql', 'Queries')
    update_query = load_sql('addresses/update_addresses.sql', 'Queries')
    check_query = load_sql('addresses/check_addresses.sql', 'Queries')

    cursor.execute(check_query)
    existing_ids = set(row[0] for row in cursor.fetchall())

    for chunk in chunked_iterable(all_addresses, 10000): 
        insert_batch = []
        update_batch = []
        for address in chunk:
            try:
                if address['addressId'] not in existing_ids:
                    deliveryAddress_values = (
                        address['addressId'],
                        address['postalcode'],
                        address['unloadingAddress'],
                        address['streetnumber'],
                        address['complement'],
                        address['remarks'],
                        address['addressType'],
                        address['contactAddress'],
                        address['shippingAddress'],
                        address['building'],
                        address['cellphone'],
                        address['town'],
                        address['appartment'],
                        address['company'],
                        address['typeQualifier'],
                        address['streetname'],
                        address['department'],
                        address['billingAddress'],
                        address['country'],
                        address['title'],
                        address['region']
                        
                    )
                    insert_batch.append(deliveryAddress_values)
                    existing_ids.add(address['addressId'])
                else:
                    update_values = (
                        address['postalcode'],
                        address['unloadingAddress'],
                        address['streetnumber'],
                        address['complement'],
                        address['remarks'],
                        address['addressType'],
                        address['contactAddress'],
                        address['shippingAddress'],
                        address['building'],
                        address['cellphone'],
                        address['town'],
                        address['appartment'],
                        address['company'],
                        address['typeQualifier'],
                        address['streetname'],
                        address['department'],
                        address['billingAddress'],
                        address['country'],
                        address['title'],
                        address['region'],
                        address['addressId']
                        )
                    update_batch.append(update_values)
            except KeyError as e:
                print(f"Missing key {e} in address: {address.get('addressId', 'Unknown')}")

        if insert_batch:
            cursor.executemany(insert_query, insert_batch)
            print(f"{len(insert_batch)} address inseridos no banco com sucesso.")
        if update_batch:
            cursor.executemany(update_query, update_batch)
            print(f"{len(update_batch)} address atualizados no banco com sucesso.")

    conn.commit()
    cursor.close()
    conn.close()