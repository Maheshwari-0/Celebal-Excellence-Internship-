import pandas as pd

order_items = pd.read_csv("DATA/order_items.csv")
print(order_items.info())
print("\nMissing Values:")
print(order_items.isnull().sum())
print("\nChecking duplicate rows...")
print("Duplicate Rows:", order_items.duplicated().sum())

print("\nChecking for negative quantities")
negative_qty=order_items[order_items["quantity"] < 0]
print(negative_qty)
print("Total negative quantity rows:", len(negative_qty))

print("\nChecking for quantity equal to 0")
zero_quantity=order_items[order_items["quantity"] == 0]
print(zero_quantity)
print("Total rows with quantity = 0:", len(zero_quantity))

print("\nRemoving rows with quantity=0")
order_items=order_items[order_items["quantity"] != 0]
print("Rows remaining:",len(order_items))

print("\nChecking for discount greater than 100%")
invalid_discount=order_items[order_items["discount_percent"] > 100]
print(invalid_discount)
print("Total invalid discounts:",len(invalid_discount))
print("\nFixing discount values greater than 100...")

order_items.loc[ order_items["discount_percent"] > 100,"discount_percent"]=100
print("Maximum discount after cleaning:",order_items["discount_percent"].max())

orders=pd.read_csv("DATA/cleaned_orders.csv")
print("\nChecking for invalid order IDs")

invalid_orders=order_items[~order_items["order_id"].isin(orders["order_id"])]
print(invalid_orders)
print("Total invalid order IDs:",len(invalid_orders))

print("\nRemoving rows with invalid order IDs")
order_items=order_items[order_items["order_id"].isin(orders["order_id"])]
print("Rows remaining:",len(order_items))

print("\nChecking invalid order IDs after cleaning")
print((~order_items["order_id"].isin(orders["order_id"])).sum())

order_items.to_csv("DATA/cleaned_order_items.csv", index=False)
print("\nCleaned order_items dataset saved successfully.")