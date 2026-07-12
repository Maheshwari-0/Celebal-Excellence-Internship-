# Delta Lake MERGE Implementation

## Objective

The objective of this assignment is to demonstrate incremental data processing using Delta Lake. The project loads customer data into a Delta table, performs basic data cleaning, simulates incremental data, applies the Delta Lake MERGE operation to update existing records and insert new records, and validates the final results.


## Dataset

### customer_master.csv
Contains the initial customer records.

Columns:
- customer_id
- name
- city
- email
- signup_date
- status

### customer_incremental.csv
Contains new customer records and updates for existing customers.

---

## Technologies Used

- Databricks
- Apache Spark (PySpark)
- Delta Lake
- SQL
- Git & GitHub

---

## Implementation Steps

### Step 1: Load Dataset
- Uploaded the customer_master.csv dataset.
- Loaded the data into a Spark DataFrame.
- Created a Delta table named `customer_master_delta`.

### Step 2: Data Cleaning
- Checked for null values.
- Removed duplicate records.
- Created a cleaned Delta table named `customer_master_cleaned`.

### Step 3: Load Incremental Dataset
- Loaded customer_incremental.csv.
- Created a Delta table named `customer_incremental_delta`.

### Step 4: Apply MERGE Operation
Performed Delta Lake MERGE to:
- Update existing customer records.
- Insert new customer records.

### Step 5: Validation
Validated the results by:
- Checking total row count.
- Checking duplicate customer IDs.
- Verifying updated records.
- Verifying inserted records.

### Step 6: Final Output
Displayed the final Delta table after the MERGE operation.

---

## MERGE Logic

- Existing customer records are updated.
- New customer records are inserted.
- The implementation follows **Slowly Changing Dimension (SCD) Type 1**, where existing records are overwritten with the latest values.

---

## Output

- Delta Table Created
- Cleaned Dataset
- Incremental Data Loaded
- MERGE Successfully Executed
- Validation Completed
- Final Customer Table Generated

---

## Learning Outcomes

- Reading CSV files using PySpark
- Creating Delta Tables
- Data Cleaning in Spark
- Delta Lake MERGE Operation
- Incremental Data Processing
- SCD Type 1 Implementation
- Data Validation
- Databricks Notebook Development

