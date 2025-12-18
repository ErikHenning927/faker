import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connections.all_connections import *
from utils.utils import load_sql, chunked_iterable

def insert_order_to_db(all_orders):
    conn = postgres_local()
    cursor = conn.cursor()

    insert_query = load_sql('orders/insert_order.sql', 'Queries')
    update_query = load_sql('orders/update_order.sql', 'Queries')
    check_query = load_sql('orders/check_order.sql', 'Queries')

    cursor.execute(check_query)
    existing_ids = set(row[0] for row in cursor.fetchall())

    for chunk in chunked_iterable(all_orders, 10000): 
        insert_batch = []
        update_batch = []
        for orderInfo in chunk:
            try:
                if orderInfo['orderId'] not in existing_ids:
                    order_values = (
                        orderInfo['orderId'], 
                        orderInfo['paymentId'], 
                        orderInfo['customerId'], 
                        orderInfo['salesChannelId'],
                        orderInfo['addressId'],
                        orderInfo['AffiliateId'], 
                        orderInfo['Description'], 
                        orderInfo['Origin'], 
                        orderInfo['deliveryQuotedCost'], 
                        orderInfo['authorizedDate'], 
                        orderInfo['invoiceShippedDate'], 
                        orderInfo['invoiceDeliveryDate'], 
                        orderInfo['date'],
                        orderInfo['statusUpdatedAt'],
                        orderInfo['paymentRefund'],
                        orderInfo['paymentRefundAttempts'],
                        orderInfo['subtotal'],
                        orderInfo['totalDiscounts'],
                        orderInfo['status'],
                        orderInfo['exportStatus'],
                        orderInfo['blockCart'],
                        orderInfo['creationDate'],
                        orderInfo['creationTime'],
                        orderInfo['modifiedDate'],
                        orderInfo['modifiedTime']
                        
                        )
                    insert_batch.append(order_values)
                    existing_ids.add(orderInfo['orderId'])
                else:
                    update_values = (
                            orderInfo['Description'], 
                            orderInfo['Origin'], 
                            orderInfo['deliveryQuotedCost'], 
                            orderInfo['authorizedDate'], 
                            orderInfo['invoiceShippedDate'], 
                            orderInfo['invoiceDeliveryDate'], 
                            orderInfo['date'],
                            orderInfo['statusUpdatedAt'],
                            orderInfo['paymentRefund'],
                            orderInfo['paymentRefundAttempts'],
                            orderInfo['subtotal'],
                            orderInfo['totalDiscounts'],
                            orderInfo['status'],
                            orderInfo['exportStatus'],
                            orderInfo['blockCart'],
                            orderInfo['creationDate'],
                            orderInfo['creationTime'],
                            orderInfo['modifiedDate'],
                            orderInfo['modifiedTime'],
                            orderInfo['orderId']
                        )
                    update_batch.append(update_values)
            except KeyError as e:
                print(f"Missing key {e} in orderId: {orderInfo.get('orderId', 'Unknown')}")

        if insert_batch:
            cursor.executemany(insert_query, insert_batch)
            print(f"{len(insert_batch)} pedidos inseridos no banco com sucesso.")
        if update_batch:
            cursor.executemany(update_query, update_batch)
            print(f"{len(update_batch)} pedidos atualizados no banco com sucesso.")

    conn.commit()
    cursor.close()
    conn.close()