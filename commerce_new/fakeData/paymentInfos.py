import random
from faker import Faker
from datetime import timedelta
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pysql.Queries.payments.insert_payment_info import insert_payment_info_to_db
from Pysql.get_ids import *
fake = Faker("pt_BR")

def generate_fake_payment_info(num_records=50):
    payments = []

    acquirers = ["Cielo", "Rede", "Stone", "PagSeguro", "Getnet"]
    groups = ["Cartão", "PIX", "Boleto"]
    connectors = ["VisaNet", "MasterCard", "Ebanx", "Adyen", "Stripe"]

    
    results = execute_query(get_paymentsmodes)
    payment_modes = [r[0] for r in results]

    for _ in range(num_records):
        creation_dt = fake.date_time_between(start_date="-1y", end_date="-1d")
        modified_dt = creation_dt + timedelta(days=random.randint(1, 150))

        installments = random.choice([1, 2, 3, 6, 10, 12])
        installment_value = round(random.uniform(10, 800), 2)
        total_value = round(installments * installment_value, 2)

        payment = {
            "paymentId": fake.uuid4(),
            "paymentModeId": random.choice(payment_modes),
            "Connector": random.choice(connectors),
            "transactionId": fake.uuid4(),
            "GiftCardId": fake.bothify(text="GC####", letters="ABCD"),
            "duplicate": random.choice([0, 1]),
            "ReferenceValue": total_value,
            "Acquirer": random.choice(acquirers),
            "Installments": installments,
            "Group": random.choice(groups),
            "MerchantName": fake.company(),
            "paidValue": total_value,
            "Nsu": str(fake.random_number(digits=8)),
            "pixRefundId": fake.uuid4(),
            "saved": random.choice([0, 1]),
            "AuthId": fake.uuid4(),
            "CardHolder": fake.name(),
            "RedemptionCode": fake.bothify("RC####"),
            "Tid": fake.uuid4(),
            "returnCode": fake.bothify("RET###"),
            "ExpiryYear": str(random.randint(2025, 2030)),
            "ReturnMessage": random.choice(["Aprovado", "Negado", "Revisão"]),
            "DueDate": fake.date_time_between(start_date="-15d", end_date="+45d"),
            "LastDigits": str(fake.random_number(digits=4)),
            "ExpiryMonth": str(random.randint(1, 12)).zfill(2),
            "InstallmentsValue": installment_value,
            "FirstDigits": str(fake.random_number(digits=6)),
            "refund": "",
            "creationDate": str(creation_dt.date()),
            "creationTime": str(creation_dt.time().replace(microsecond=0)),
            "modifiedDate": str(modified_dt.date()),
            "modifiedTime": str(modified_dt.time().replace(microsecond=0)),
        }

        payments.append(payment)

    return payments


# Exemplo de uso
data = generate_fake_payment_info(20000)
insert_payment_info_to_db(data)
