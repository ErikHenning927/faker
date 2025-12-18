import random
from faker import Faker
from datetime import timedelta
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Pysql.Queries.warehouse.insert_warehouse import *

fake = Faker("pt_BR")

def generate_fake_warehouse_data(num_records=50):
    warehouses = []
    workflow_names = [
        "Workflow-Padrao",
        "Workflow-Expresso",
        "Workflow-Reverso",
        "Workflow-Picking-1",
        "Workflow-Picking-2"
    ]

    for _ in range(num_records):
        creation_dt = fake.date_time_between(start_date="-2y", end_date="-1y")
        modified_dt = creation_dt + timedelta(days=random.randint(1, 300))

        warehouse = {
            "warehouseId": f"WH{fake.unique.random_number(digits=3)}",
            "default": random.choice([0, 1]),
            "name": fake.city() + " - Centro de Distribuição",
            "isAllowRestock": random.choice([0, 1]),
            "external": random.choice([0, 1]),
            "priority": str(random.randint(1, 10)),
            "warehouseBinTransferWorkflowName": random.choice(workflow_names),
            "score": round(random.uniform(1, 10), 2),
            "creationDate": str(creation_dt.date()),
            "creationTime": str(creation_dt.time().replace(microsecond=0)),
            "modifiedDate": str(modified_dt.date()),
            "modifiedTime": str(modified_dt.time().replace(microsecond=0)),
        }
        
        warehouses.append(warehouse)

    return warehouses

data = generate_fake_warehouse_data(200)
insert_warehouse_to_db(data)
