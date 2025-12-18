import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connections.all_connections import *
from utils.utils import load_sql, chunked_iterable

def insert_payment_info_to_db(all_paymentInfos):
    conn = db_local()
    cursor = conn.cursor()

    insert_query = load_sql('payments/insert_paymentInfo.sql', 'Queries')
    update_query = load_sql('payments/update_paymentInfo.sql', 'Queries')
    check_query = load_sql('payments/check_paymentInfo.sql', 'Queries')

    cursor.execute(check_query)
    existing_ids = set(row[0] for row in cursor.fetchall())

    for chunk in chunked_iterable(all_paymentInfos, 10000): 
        insert_batch = []
        update_batch = []
        for paymentInfo in chunk:
            try:
                if paymentInfo['paymentId'] not in existing_ids:
                    paymentInfo_values = (
                        paymentInfo.get('paymentId', None),
                        paymentInfo.get('paymentModeId', None),
                        paymentInfo.get('Connector', None),
                        paymentInfo.get('transactionId', None),
                        paymentInfo.get('GiftCardId', None),
                        paymentInfo.get('duplicate', None),
                        paymentInfo.get('ReferenceValue', None),
                        paymentInfo.get('Acquirer', None),
                        paymentInfo.get('Installments', None),
                        paymentInfo.get('Group', None),
                        paymentInfo.get('MerchantName', None),
                        paymentInfo.get('paidValue', None),
                        paymentInfo.get('Nsu', None),
                        paymentInfo.get('pixRefundId', None),
                        paymentInfo.get('saved', None),
                        paymentInfo.get('AuthId', None),
                        paymentInfo.get('CardHolder', None),
                        paymentInfo.get('RedemptionCode', None),
                        paymentInfo.get('Tid', None),
                        paymentInfo.get('returnCode', None),
                        paymentInfo.get('ExpiryYear', None),
                        paymentInfo.get('ReturnMessage', None),
                        paymentInfo.get('DueDate', None),
                        paymentInfo.get('LastDigits', None),
                        paymentInfo.get('ExpiryMonth', None),
                        paymentInfo.get('InstallmentsValue', None),
                        paymentInfo.get('FirstDigits', None),
                        paymentInfo.get('refund', None),
                        paymentInfo.get('creationDate', None),
                        paymentInfo.get('creationTime', None),
                        paymentInfo.get('modifiedDate', None),
                        paymentInfo.get('modifiedTime', None)
                    )
            
                    insert_batch.append(paymentInfo_values)
                    existing_ids.add(paymentInfo['paymentId'])
                else:
                    update_values = (
                        
                        paymentInfo.get('paymentModeId', None),
                        paymentInfo.get('Connector', None),
                        paymentInfo.get('transactionId', None),
                        paymentInfo.get('GiftCardId', None),
                        paymentInfo.get('duplicate', None),
                        paymentInfo.get('ReferenceValue', None),
                        paymentInfo.get('Acquirer', None),
                        paymentInfo.get('Installments', None),
                        paymentInfo.get('Group', None),
                        paymentInfo.get('MerchantName', None),
                        paymentInfo.get('paidValue', None),
                        paymentInfo.get('Nsu', None),
                        paymentInfo.get('pixRefundId', None),
                        paymentInfo.get('saved', None),
                        paymentInfo.get('AuthId', None),
                        paymentInfo.get('CardHolder', None),
                        paymentInfo.get('RedemptionCode', None),
                        paymentInfo.get('Tid', None),
                        paymentInfo.get('returnCode', None),
                        paymentInfo.get('ExpiryYear', None),
                        paymentInfo.get('ReturnMessage', None),
                        paymentInfo.get('DueDate', None),
                        paymentInfo.get('LastDigits', None),
                        paymentInfo.get('ExpiryMonth', None),
                        paymentInfo.get('InstallmentsValue', None),
                        paymentInfo.get('FirstDigits', None),
                        paymentInfo.get('refund', None),
                        paymentInfo.get('creationDate', None),
                        paymentInfo.get('creationTime', None),
                        paymentInfo.get('modifiedDate', None),
                        paymentInfo.get('modifiedTime', None),
                        paymentInfo.get('paymentId', None)
                        )
                    update_batch.append(update_values)
            except KeyError as e:
                print(f"Missing key {e} in paymentInfo: {paymentInfo.get('paymentId', 'Unknown')}")

        if insert_batch:
            cursor.executemany(insert_query, insert_batch)
            print(f"{len(insert_batch)} modos de pagamentos inseridos no banco com sucesso.")
        if update_batch:
            cursor.executemany(update_query, update_batch)
            print(f"{len(update_batch)} modos de pagamentos atualizados no banco com sucesso.")

    conn.commit()
    cursor.close()
    conn.close()