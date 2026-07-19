import pandas as pd

orders = pd.read_csv("DATA/orders.csv")
print(orders.head(10))
print(orders.info())
print("\nMissing Values:")
print(orders.isnull().sum())
print("\nChecking duplicate rows")
print("Duplicate Rows:", orders.duplicated().sum())

print("\nChecking rows with missing customer IDs")
missing_customer = orders[orders["customer_id"].isnull()]
print(missing_customer)
print("Total missing customer IDs:", len(missing_customer))

print("\nCustomer ID datatype:")
print(orders["customer_id"].dtype)
orders["customer_id"] = orders["customer_id"].astype("Int64")

print("\nChecking order_date datatype")
print(orders["order_date"].dtype)

print("\nConverting order_date to datetime")
orders["order_date"] = pd.to_datetime(orders["order_date"],format="mixed",
    dayfirst=True,errors="coerce")

print("\nChecking for invalid dates")
invalid_dates = orders[orders["order_date"].isnull()]
print(invalid_dates)
print("Total invalid dates:", len(invalid_dates))

print("\nChecking duplicate Order IDs")
duplicate_order_ids = orders["order_id"].duplicated().sum()
print("Duplicate Order IDs:", duplicate_order_ids)

print("\nChecking region codes")
print(orders["region_code"].value_counts())

orders.to_csv("DATA/cleaned_orders.csv", index=False)
print("\nCleaned orders dataset saved successfully.")