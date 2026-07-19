import pandas as pd

products = pd.read_csv("DATA/products.csv")
print(products.info())
print(products.isnull().sum())
print(products.duplicated().sum())
print(products["product_name"].head(20))

# Removing extra spaces
products["product_name"] = products["product_name"].str.strip()
products["category"] = products["category"].str.strip()
products["subcategory"] = products["subcategory"].str.strip()

#printing the updated data
print(products["product_name"].head(20))

print("Duplicate Product IDs:", products["product_id"].duplicated().sum())

print("\nChecking for products with invalid cost price<= 0:")
print(products[products["cost_price"] <= 0])

print("\nChecking duplicate product names")
duplicates = products[products.duplicated(subset=["product_name"], keep=False)]
print(duplicates)

products.to_csv("DATA/cleaned_products.csv", index=False)
print("\n Cleaned products dataset saved successfully.")


