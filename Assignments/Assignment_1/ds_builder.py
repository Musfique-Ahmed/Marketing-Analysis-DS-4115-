import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

# 1. Products Master Table
product_ids = [f"P{str(i).zfill(3)}" for i in range(1, 51)]
product_names = [f"Product {i}" for i in range(1, 51)]
unit_prices = [round(random.uniform(10.0, 250.0), 2) for _ in range(50)]

pd.DataFrame({
    "Product ID": product_ids,
    "Product Name": product_names,
    "Unit Price": unit_prices
}).to_csv("Products.csv", index=False)

# 2. Marketing Spend Master Table
channels = ["Google Ads", "Meta Ads", "Organic Search", "Email", "Affiliates"]
pd.DataFrame({
    "Acquisition Channel": channels,
    "Total Spend": [25000, 30000, 5000, 10000, 15000],
    "New Customers Acquired": [1200, 1500, 800, 900, 1100]
}).to_csv("Marketing_Spend.csv", index=False)

# 3. 100,000+ Rows Transaction Dataset
num_rows = 105000
start_date = datetime(2025, 1, 1)

pd.DataFrame({
    "Transaction ID": [f"TXN{str(i).zfill(7)}" for i in range(1, num_rows + 1)],
    "Customer ID": [f"CUST{random.randint(1000, 9999)}" for _ in range(num_rows)],
    "Date": [(start_date + timedelta(days=random.randint(0, 364))).strftime("%Y-%m-%d") for _ in range(num_rows)],
    "Product ID": [random.choice(product_ids) for _ in range(num_rows)],
    "Units Sold": [random.randint(1, 5) for _ in range(num_rows)],
    "Acquisition Channel": [random.choice(channels) for _ in range(num_rows)]
}).to_csv("Transactions.csv", index=False)

print("Dataset generated successfully!")
