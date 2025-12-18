import random
from faker import Faker
from datetime import timedelta
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Pysql.Queries.customer.insert_customer_info import * 
fake = Faker("pt_BR")

def generate_fake_customer_info(num_records=50):
    customers = []

    for _ in range(num_records):
        creation_dt = fake.date_time_between(start_date="-2y", end_date="-1y")
        modified_dt = creation_dt + timedelta(days=random.randint(1, 300))

        cpf = fake.unique.numerify(text="###########")


        customer = {
            "customerId": f"CUST{fake.unique.random_number(digits=5)}",
            "customerDocument": cpf,
            "customerFirstName": fake.first_name(),
            "customerLastName": fake.last_name(),
            "customerDocumentType": "CPF",
            "customerPhone": fake.phone_number(),
            "customerEmail": fake.email(),
            "customerTradeName": fake.company(),
            "customerCorporateDocument": fake.cnpj(),
            "customerStateInscription": fake.random_number(digits=9),
            "customerCorporatePhone": fake.phone_number(),
            "customerIsCorporate": random.choice([0, 1]),
            "customerUserProfileId": fake.uuid4(),
            "customerUserProfileVersion": str(random.randint(1, 10)),
            "customerClass": random.choice(["B2C", "B2B"]),
            "customerCode": f"C{fake.random_number(digits=5)}",
        }

        customers.append(customer)

    return customers

