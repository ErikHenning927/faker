import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connections.all_connections import db_local
from utils.utils import load_sql, chunked_iterable

def insert_warehouse_to_db(all_warehouses):
    conn = db_local()
    cursor = conn.cursor()

    insert_query = load_sql('warehouse/insert_warehouse.sql', 'Queries')
    update_query = load_sql('warehouse/update_warehouse.sql', 'Queries')
    check_query = load_sql('warehouse/check_warehouse.sql', 'Queries')

    cursor.execute(check_query)
    existing_ids = set(row[0] for row in cursor.fetchall())

    for chunk in chunked_iterable(all_warehouses, 10000): 
        insert_batch = []
        update_batch = []
        for warehouse in chunk:
            try:
                if warehouse['warehouseId'] not in existing_ids:
                    warehouse_values = (
                        warehouse['warehouseId'],
                        warehouse['default'],
                        warehouse['name'],
                        warehouse['isAllowRestock'],
                        warehouse['external'],
                        warehouse['priority'],
                        warehouse['warehouseBinTransferWorkflowName'],
                        warehouse['score'],
                        warehouse['creationDate'],
                        warehouse['creationTime'],
                        warehouse['modifiedDate'],
                        warehouse['modifiedTime']

                    )
                    insert_batch.append(warehouse_values)
                    existing_ids.add(warehouse['warehouseId'])
                else:
                    update_values = (
                            warehouse['default'],
                            warehouse['name'],
                            warehouse['isAllowRestock'],
                            warehouse['external'],
                            warehouse['priority'],
                            warehouse['warehouseBinTransferWorkflowName'],
                            warehouse['score'],
                            warehouse['creationDate'],
                            warehouse['creationTime'],
                            warehouse['modifiedDate'],
                            warehouse['modifiedTime'],
                            warehouse['warehouseId']
                        )
                    update_batch.append(update_values)
            except KeyError as e:
                print(f"Missing key {e} in warehouse: {warehouse.get('warehouseId', 'Unknown')}")

        if insert_batch:
            cursor.executemany(insert_query, insert_batch)
            print(f"{len(insert_batch)} depósitos inseridos no banco com sucesso.")
        if update_batch:
            cursor.executemany(update_query, update_batch)
            print(f"{len(update_batch)} depósitos atualizados no banco com sucesso.")

    conn.commit()
    cursor.close()
    conn.close()