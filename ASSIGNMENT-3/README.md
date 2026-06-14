# Superstore Sales Analysis Using SQL

## Introduction

In this Assignment, I analyzed the Superstore Sales dataset using SQL. The main objective was to practice and understand important SQL concepts such as Subqueries, Common Table Expressions (CTEs), Window Functions, Joins, and Aggregations while solving real business problems.
The dataset contains information about customers, orders, products, sales, discounts, and profits. Using this data, I created a simple database structure and performed various analyses to gain insights into customer purchasing behavior and sales performance.

## Dataset Information

The dataset includes:

* Customer details
* Product details
* Order details
* Sales and profit information
* Shipping information

The raw dataset was first loaded into a table named `superstore_raw`.

## Database Design

To make the data more organized, I divided the raw dataset into three tables:

### Customers Table

Stores customer-related information such as:
* Customer ID
* Customer Name
* Segment
* Country
* City
* State
* Postal Code
* Region

### Products Table
Stores product-related information such as:
* Product ID
* Category
* Sub-Category
* Product Name

### Orders Table
Stores transaction-related information such as:
* Order ID
* Order Date
* Ship Date
* Ship Mode
* Customer ID
* Product ID
* Sales
* Quantity
* Discount
* Profit

## SQL Concepts Used
During this project, I worked with:
* SELECT statements
* GROUP BY
* Aggregate Functions
* JOINS
* Subqueries
* Common Table Expressions (CTEs)
* Window Functions
* RANK()
* ROW_NUMBER()

## Business Questions Solved
I answered the following business questions using SQL:

1. Find all orders where sales are greater than the average sales.
2. Find the highest sales order for each customer.
3. Calculate total sales for each customer.
4. Find customers whose total sales are above average.
5. Rank customers based on total sales.
6. Assign row numbers to each order within a customer.
7. Display the top 3 customers based on total sales.

### Customer Sales Insights
* Who are the top 5 customers?
* Who are the bottom 5 customers?
* Which customers made only one order?
* Which customers have above-average sales?
* What is the highest order value per customer?

## Key Learnings

Through this Assignment, I learned how to:
* Normalize raw data into multiple tables.
* Use SQL joins to combine data from different tables.
* Apply subqueries to solve business problems.
* Use CTEs to simplify complex queries.
* Use window functions such as RANK() and ROW_NUMBER().
* Generate meaningful business insights from sales data.
## Conclusion

This project helped me strengthen my SQL skills by working on a real-world retail dataset. I gained hands-on experience with database design, query writing, and business analysis. The project also demonstrated how SQL can be used to transform raw data into actionable insights for decision making.
