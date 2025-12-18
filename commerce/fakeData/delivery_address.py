import random
from faker import Faker
from datetime import timedelta
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pysql.Queries.addresses.insert_address_info import insert_address_to_db

fake = Faker("pt_BR")


def generate_fake_address_data(num_records=50):
    addresses = []

    for _ in range(num_records):
        creation_dt = fake.date_time_between(start_date="-1y", end_date="-1d")
        modified_dt = creation_dt + timedelta(days=random.randint(1, 150))

        address = {
            "addressId": fake.uuid4(),
            "postalcode": fake.postcode(),
            "unloadingAddress": random.choice([0, 1]),
            "streetnumber": fake.building_number(),
            "complement": fake.building_number() + " " + random.choice(["Apt", "Sala", "Bloco", "Casa"]),
            "remarks": fake.text(30),
            "addressType": random.choice(["Residencial", "Comercial"]),
            "contactAddress": random.choice([0, 1]),
            "shippingAddress": random.choice([0, 1]),
            "building": fake.word(),
            "cellphone": fake.phone_number(),
            "town": fake.city(),
            "appartment": fake.random_number(digits=3),
            "company": fake.company(),
            "typeQualifier": "BR",
            "streetname": fake.street_name(),
            "department": fake.random_number(digits=3),
            "billingAddress": random.choice([0, 1]),
            "country": "BR",
            "title": fake.prefix(),
            "region": fake.state(),
            "creationDate": str(creation_dt.date()),
            "creationTime": str(creation_dt.time().replace(microsecond=0)),
            "modifiedDate": str(modified_dt.date()),
            "modifiedTime": str(modified_dt.time().replace(microsecond=0)),
        }

        addresses.append(address)

    return addresses

# Exemplo
data = generate_fake_address_data(20000)
insert_address_to_db(data)
