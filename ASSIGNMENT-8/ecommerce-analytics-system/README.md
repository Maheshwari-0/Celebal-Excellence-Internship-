# E-Commerce Analytics System

## Project Overview

The E-Commerce Analytics System is a Python and SQLite based analytics project that performs data cleaning, SQL analysis, business reporting, and customer analytics on an e-commerce dataset.
The project demonstrates SQL concepts ranging from basic queries to advanced analytical functions such as Window Functions, Common Table Expressions (CTEs), Ranking Functions, Cohort Analysis, and Customer Segmentation.

---

## Technologies Used

- Python 3
- SQLite3
- SQL
- VS Code

---

## Project Structure

```
ECOMMERCE-ANALYTICS-SYSTEM
│
├── data
│   ├── customers.csv
│   ├── orders.csv
│   ├── order_items.csv
│   ├── products.csv
│   ├── cleaned_customers.csv
│   ├── cleaned_orders.csv
│   ├── cleaned_order_items.csv
│   └── cleaned_products.csv
│
├── src
│   ├── data_cleaning
│   ├── database
│   ├── sql_analysis.py
│   ├── ecommerce_report_generator.py
│   └── test_cases.py
│
├── ecommerce.db
├── main.py
└── README.md
```

---

## Features

### Data Cleaning

- Removed duplicate records
- Handled missing values
- Standardized product names
- Corrected invalid values
- Cleaned date formats

---

### SQL Analysis

The project contains SQL queries covering:

#### Basic Queries

- Total revenue per category
- Top customers by revenue
- Monthly order count

#### Intermediate Queries

- Customers with no delivered orders
- Products with more returns than purchases
- Return rate by category

#### Advanced Queries

- Running totals using Window Functions
- Product ranking using DENSE_RANK()
- Customer purchase gap using LAG()
- Multi-level CTEs
- NTILE customer segmentation
- Year-over-Year revenue comparison
- First and Last category analysis
- Cumulative revenue distribution
- Cohort Analysis
- Frequently bought together products

---

### Report Generator

A command-line reporting tool built using Python and SQLite.

Features:

- Daily reports
- Weekly reports
- Monthly reports
- Revenue summary
- Total orders
- Unique customers
- Top 3 products
- Previous period comparison

---

### Edge Case Testing

Python test cases verify:

- Invalid Order IDs
- Discount greater than 100%
- Zero quantity orders
- Future order dates

---

## Database Tables

- Customers
- Orders
- Order Items
- Products

---

## How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```
---
### 2. Open the project
```bash
cd ECOMMERCE-ANALYTICS-SYSTEM
```
---

### 3. Run SQL Analysis

```bash
python src/sql_analysis.py
```
---
### 4. Run Report Generator

```bash
python src/ecommerce_report_generator.py
```

---

### 5. Run Test Cases

```bash
python src/test_cases.py
```

---

## Sample Report

```
===== E-Commerce Report =====

Report Type : Monthly

Date Range :
2025-01-01 to 2025-01-31

Summary
Total Orders : 42
Revenue : 215430.75
Unique Customers : 39
Top Products
1. Aster Charger Cable
2. Urban Cotton T-Shirt
3. Nova LED Lamp

Comparison with Previous Period
Oders Change : +15.38%
Revenue Change : +8.94%
Customer Change : +11.43%
```

---

## SQL Concepts Covered

- SELECT
- WHERE
- GROUP BY
- ORDER BY
- HAVING
- JOIN
- INNER JOIN
- LEFT JOIN
- Aggregate Functions
- CASE Statements
- Common Table Expressions (CTEs)
- Window Functions
- FIRST_VALUE()
- LAG()
- DENSE_RANK()
- NTILE()
- Self Join
- Date Functions

---

## Learning Outcomes

Through this project, the following concepts were implemented:

- Data Cleaning using SQL and Python
- SQLite Database Management
- Complex SQL Query Writing
- Business Analytics
- Customer Segmentation
- Sales Reporting
- Cohort Analysis
- Window Functions
- Command-Line Application Development
- Edge Case Testing