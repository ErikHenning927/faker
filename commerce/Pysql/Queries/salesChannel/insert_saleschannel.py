import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connections.all_connections import *
from utils.utils import load_sql, chunked_iterable

def insert_salesChannel_to_db(all_salesChannels):
    conn = db_local()
    cursor = conn.cursor()

    insert_query = load_sql('salesChannel/insert_salesChannel.sql', 'Queries')
    update_query = load_sql('salesChannel/update_salesChannel.sql', 'Queries')
    check_query = load_sql('salesChannel/check_salesChannel.sql', 'Queries')

    cursor.execute(check_query)
    existing_ids = set(row[0] for row in cursor.fetchall())

    for chunk in chunked_iterable(all_salesChannels, 10000): 
        insert_batch = []
        update_batch = []
        for salesChannel in chunk:
            try:
                if salesChannel['salesChannelId'] not in existing_ids:
                    salesChannel_values = (
                        salesChannel['salesChannelId'],
                        salesChannel['stateRegistration'],
                        salesChannel['ownStore'],
                        salesChannel['cnpj'],
                        salesChannel['name'],
                        salesChannel['active'],
                        salesChannel['creationDate'],
                        salesChannel['creationTime'],
                        salesChannel['modifiedDate'],
                        salesChannel['modifiedTime']
                    )
                    insert_batch.append(salesChannel_values)
                    existing_ids.add(salesChannel['salesChannelId'])
                else:
                    update_values = (
                            salesChannel['stateRegistration'],
                            salesChannel['ownStore'],
                            salesChannel['cnpj'],
                            salesChannel['name'],
                            salesChannel['active'],
                            salesChannel['creationDate'],
                            salesChannel['creationTime'],
                            salesChannel['modifiedDate'],
                            salesChannel['modifiedTime'],
                            salesChannel['salesChannelId']
                        )
                    update_batch.append(update_values)
            except KeyError as e:
                print(f"Missing key {e} in salesChannel: {salesChannel.get('salesChannelId', 'Unknown')}")

        if insert_batch:
            cursor.executemany(insert_query, insert_batch)
            print(f"{len(insert_batch)} canais de vendas inseridos no banco com sucesso.")
        if update_batch:
            cursor.executemany(update_query, update_batch)
            print(f"{len(update_batch)} canais de vendas atualizados no banco com sucesso.")

    conn.commit()
    cursor.close()
    conn.close()