import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connections.all_connections import *
from utils.utils import load_sql, chunked_iterable

def insert_paymentModes_to_db(all_paymentModes):
    conn = postgres_local()
    cursor = conn.cursor()

    insert_query = load_sql('paymentModes/insert_paymentMode.sql', 'Queries')
    update_query = load_sql('paymentModes/update_paymentMode.sql', 'Queries')
    check_query = load_sql('paymentModes/check_paymentMode.sql', 'Queries')

    cursor.execute(check_query)
    existing_ids = set(row[0] for row in cursor.fetchall())

    for chunk in chunked_iterable(all_paymentModes, 10000): 
        insert_batch = []
        update_batch = []
        for paymentMode in chunk:
            try:
                if paymentMode['paymentModeId'] not in existing_ids:
                    paymentMode_values = (
                        paymentMode['paymentModeId'],
                        paymentMode['name'],
                        paymentMode['description'],
                        paymentMode['active'],
                        paymentMode['refundBy'],
                        paymentMode['creationDate'],
                        paymentMode['creationTime'],
                        paymentMode['modifiedDate'],
                        paymentMode['modifiedTime']
                    )
            
                    insert_batch.append(paymentMode_values)
                    existing_ids.add(paymentMode['paymentModeId'])
                else:
                    update_values = (
                        paymentMode['name'],
                        paymentMode['description'],
                        paymentMode['active'],
                        paymentMode['refundBy'],
                        paymentMode['creationDate'],
                        paymentMode['creationTime'],
                        paymentMode['modifiedDate'],
                        paymentMode['modifiedTime'],
                        paymentMode['paymentModeId']
                        )
                    update_batch.append(update_values)
            except KeyError as e:
                print(f"Missing key {e} in paymentMode: {paymentMode.get('paymentModeId', 'Unknown')}")

        if insert_batch:
            cursor.executemany(insert_query, insert_batch)
            print(f"{len(insert_batch)} modos de pagamentos inseridos no banco com sucesso.")
        if update_batch:
            cursor.executemany(update_query, update_batch)
            print(f"{len(update_batch)} modos de pagamentos atualizados no banco com sucesso.")

    conn.commit()
    cursor.close()
    conn.close()