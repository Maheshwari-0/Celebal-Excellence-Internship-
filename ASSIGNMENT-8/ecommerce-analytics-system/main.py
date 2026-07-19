import pandas as pd
customers = pd.read_csv("DATA/customers.csv")
products = pd.read_csv("DATA/products.csv")
orders = pd.read_csv("DATA/orders.csv")
order_items = pd.read_csv("DATA/order_items.csv")
print("Customers:", customers.shape)
print("Products:", products.shape)
print("Orders:", orders.shape)
print("Order Items:", order_items.shape)