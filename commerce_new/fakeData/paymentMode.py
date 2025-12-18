import random
from faker import Faker
from datetime import timedelta
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Pysql.Queries.paymentModes.insert_paymentMode import *  
fake = Faker("pt_BR")

def generate_fake_payment_mode_data(num_records=50):
    payment_modes = []
    for _ in range(num_records):
        creation_dt = fake.date_time_between(start_date="-2y", end_date="-1y")
        modified_dt = creation_dt + timedelta(days=random.randint(1, 300))

        payment_mode = {
            "paymentModeId": f"PM{fake.unique.random_number(digits=3)}",
            "name": fake.word().capitalize() + " Pagamento",
            "description": fake.sentence(nb_words=6),
            "active": random.choice([0, 1]),
            "refundBy": random.choice([0, 1, 2]),  # ex: 0 = system, 1 = manual, 2 = automatic
            "creationDate": str(creation_dt.date()),
            "creationTime": str(creation_dt.time().replace(microsecond=0)),
            "modifiedDate": str(modified_dt.date()),
            "modifiedTime": str(modified_dt.time().replace(microsecond=0)),
        }
        
        payment_modes.append(payment_mode)

    return payment_modes

