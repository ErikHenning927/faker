from paymentMode import *
from customerData import *
from delivery_address import *
from salesChannels import *
from warehouse import *
from paymentInfos import *
from orders import *

# insert Payment Mode
data = generate_fake_payment_mode_data(10)
insert_paymentModes_to_db(data)

# Insert Customer Info
data = generate_fake_customer_info(10000)
insert_customer_info_to_db(data)

# Insert Address Info
data = generate_fake_address_data(20000)
insert_address_to_db(data)

# Insert Sales Channel Info
data = generate_fake_sales_channel(20)
insert_salesChannel_to_db(data)

# Insert Warehouse Info
data = generate_fake_warehouse_data(200)
insert_warehouse_to_db(data)

# Insert Payment Info
data = generate_fake_payment_info(20000)
insert_payment_info_to_db(data)

# Insert Orders Info
data = generate_fake_orders_data(20000)
insert_order_to_db(data)
