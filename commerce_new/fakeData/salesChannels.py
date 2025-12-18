import random
from faker import Faker
from datetime import timedelta
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Pysql.Queries.salesChannel.insert_saleschannel import *

fake = Faker("pt_BR")

def generate_fake_sales_channel(num_records=50):
    records = []

    for _ in range(num_records):
        creation_dt = fake.date_time_between(start_date='-2y', end_date='now')
        modified_dt = creation_dt + timedelta(days=random.randint(0, 300))

        record = {
            "salesChannelId": random.randint(1, 10),
            "stateRegistration": fake.ean(length=13),  # Usando EAN como IE fictícia
            "ownStore": random.randint(0, 1),
            "cnpj": fake.cnpj(),
            "name": fake.company(),
            "active": random.randint(0, 1),
            "creationDate": creation_dt.date().isoformat(),
            "creationTime": creation_dt.time().replace(microsecond=0).isoformat(),
            "modifiedDate": modified_dt.date().isoformat(),
            "modifiedTime": modified_dt.time().replace(microsecond=0).isoformat()
        }

        records.append(record)

    return records
