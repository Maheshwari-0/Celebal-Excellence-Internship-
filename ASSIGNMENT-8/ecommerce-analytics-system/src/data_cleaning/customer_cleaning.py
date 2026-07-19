#Cleaning the Customers Dataset
import pandas as pd

customers = pd.read_csv("DATA/customers.csv")

# Dataset information
print(customers.info())
print("\nMissing Values:")
print(customers.isnull().sum())

print("\nChecking duplicate rows...")
duplicate_rows = customers.duplicated().sum()
print("Duplicate Rows:", duplicate_rows)

print("\nChecking for invalid email addresses:")
invalid_email = customers[
    ~customers["email"].str.contains(
     r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",regex=True
    )
]
print(invalid_email)
print("Total invalid emails:", len(invalid_email))

print("\nInvalid email addresses:")
print(invalid_email[["customer_id", "email"]])

print("\nFixing invalid email addresses")
customers["email"] = customers["email"].str.replace(
    r"(?<!@)example\.com$","@example.com",regex=True
)
customers["email"] = customers["email"].str.replace( r"@$","@example.com",regex=True
)


invalid_email = customers[
    ~customers["email"].str.contains(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
        regex=True
    )
]
print(invalid_email[["customer_id", "email"]])
print("Total invalid emails:", len(invalid_email))


print("\nConverting registration_date to datetime")
customers["registration_date"] = pd.to_datetime(customers["registration_date"],errors="coerce"
)
print("Invalid dates:", customers["registration_date"].isnull().sum())

print("\nChecking duplicate customer IDs")
print("Duplicate Customer IDs:", customers["customer_id"].duplicated().sum())


print("\nRemoving extra spaces from text columns")
customers["customer_name"] = customers["customer_name"].str.strip()
customers["email"] = customers["email"].str.strip()
customers["customer_type"] = customers["customer_type"].str.strip()

print("\nStandardizing customer types")
customers["customer_type"] = customers["customer_type"].str.upper()
print(customers["customer_type"].value_counts())

customers.to_csv("DATA/cleaned_customers.csv", index=False)
print("\nCleaned customers dataset saved successfully.")