import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")
customers = pd.read_csv("DATA/cleaned_customers.csv")
products = pd.read_csv("DATA/cleaned_products.csv")
orders = pd.read_csv("DATA/cleaned_orders.csv")
order_items = pd.read_csv("DATA/cleaned_order_items.csv")
customers.to_sql("customers", conn, if_exists="replace", index=False)
products.to_sql("products", conn, if_exists="replace", index=False)
orders.to_sql("orders", conn, if_exists="replace", index=False)
order_items.to_sql("order_items", conn, if_exists="replace", index=False)
conn.commit()
conn.close()

print("Database created successfully.")