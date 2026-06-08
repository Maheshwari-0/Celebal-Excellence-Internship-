### ASSIGNMENT-1  SUMMARY 
Name: Maheshwari Dothre
Topic: Basic Data Exploration and Cleaning using Pandas
### Dataset Used:
 I used  Kaggle which contains product listings from an e-commerce platform. The dataset had 1000 rows and 24 columns including product details like title, category, price, discount, rating, and seller information.
### Step 1 - Loading the Dataset 
I loaded the CSV file into a Pandas DataFrame using pd.read_csv(). This converts the raw CSV file into a table-like structure that Python can work with easily.
### Step 2 - Exploring the Dataset
 I explored the dataset using head(), tail(), shape, columns, dtypes and describe(). This helped me understand the structure of the data, what columns exist, what type of values they hold, and basic statistics like min, max and average values.
### Step 3 - Handling Missing Values 
When I checked for missing values using isnull().sum(), I found 2639 missing values across 6 columns. 
‘what_customers_said' had 573 missing values (57%),dropped the column since more than half the data was missing.
 'videos' had 781 missing values (78%)  — dropped the column .
 'variations' had 562 missing values (56%) — dropped the column .
'discount' had 121 missing values — filled with 0 since no discount means 0% off .
'seller_name' had 301 missing values — filled with 'Unknown' .
'seller_information' had 301 missing values — filled with 'Not Available'.
### Step 4 - Filtering Rows and Selecting Columns
Filtered rows by rating, discount, category Selected specific columns for analysis
### Step 5 - Removing Duplicates 
I checked for duplicate rows using duplicated().sum() and also checked specifically for duplicate product IDs. The dataset had 0 duplicate rows, meaning the data was already clean. I still applied drop_duplicates() as a best practice to ensure data integrity.
### Step 6 - Creating a Derived Column
Cleaned final_price column (removed ₹ symbol) 
Created quantity = 1
Created total_amount = final_price × quantity
### Step 7 - Saving the Cleaned Dataset
Finally I saved the cleaned DataFrame as a new CSV file called ‘cleaned_Combined_dataset.csv’ using df.to_csv(). I made sure to use index=False so that the row numbers are not saved as an extra column. I verified the saved file by re-reading it and confirming the shape was correct.
### What I Learned: 
This assignment taught me how real world datasets are messy and require cleaning before analysis. I learned how to identify and handle missing values, when to drop vs fill them, how to filter data based on conditions, and how to create new useful columns from existing ones. I also learned that data types matter a lot, the price column looked like a number but was actually stored as text which caused calculation errors until I fixed it.