import random
from faker import Faker
from datetime import timedelta
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Pysql.Queries.orders.insert_order import *
from Pysql.get_ids import *


fake = Faker("pt_BR")

def generate_fake_orders_data(num_records=50):
    orders = []

    statuses = ["Pago", "Faturado", "Cancelado", "Enviado", "Entregue"]
    origins = ["E-commerce", "Marketplace", "App"]

    payments = execute_query(get_paymentids)
    payments_ids = [r[0] for r in payments]

    adress = execute_query(get_address_ids)
    address_ids = [r[0] for r in adress]

    customers = execute_query(get_customer_ids)
    customer_ids = [r[0] for r in customers]

    sales = execute_query(get_sales_channel_ids)
    sales_channel_ids = [r[0] for r in sales]

    
    for _ in range(num_records):
        creation_dt = fake.date_time_between(start_date="-6m", end_date="-3m")
        modified_dt = creation_dt + timedelta(days=random.randint(1, 30))

        authorized = creation_dt + timedelta(hours=random.randint(1, 24))
        shipped = authorized + timedelta(days=random.randint(1, 7))
        delivered = shipped + timedelta(days=random.randint(1, 10))

        subtotal = round(random.uniform(20, 5000), 2)
        discounts = round(random.uniform(0, subtotal * 0.3), 2)


        order = {
            "orderId": f"ORD{fake.unique.random_number(digits=7)}",
            "paymentId": random.choice(payments_ids),
            "customerId": random.choice(customer_ids),
            "addressId": random.choice(address_ids),
            "salesChannelId": random.choice(sales_channel_ids),
            "Origin": random.choice(origins),
            "AffiliateId": fake.uuid4(),
            "Description": fake.sentence(nb_words=4),
            "deliveryQuotedCost": round(random.uniform(5, 100), 2),
            "invoiceShippedDate": shipped,
            "invoiceDeliveryDate": delivered,
            "authorizedDate": authorized,
            "date": creation_dt,
            "statusUpdatedAt": modified_dt,
            "paymentRefund": random.randint(0, 1),
            "paymentRefundAttempts": random.randint(0, 3),
            "subtotal": subtotal,
            "totalDiscounts": discounts,
            "status": random.choice(statuses),
            "exportStatus": random.choice(["OK", "PENDING", "ERROR"]),
            "blockCart": random.choice([0, 1]),
            "creationDate": str(creation_dt.date()),
            "creationTime": str(creation_dt.time().replace(microsecond=0)),
            "modifiedDate": str(modified_dt.date()),
            "modifiedTime": str(modified_dt.time().replace(microsecond=0)),
        }

        orders.append(order)

    return orders

# Exemplo
data = generate_fake_orders_data(20000)
insert_order_to_db(data)