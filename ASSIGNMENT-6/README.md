# Spark Week 6 Assignment

## Overview

This repository contains the solutions for the **Week 6 Apache Spark Assignment** completed using **PySpark in Databricks**. The assignment covers Spark architecture, DataFrame operations, Parquet, lazy evaluation, transformations and actions, and query execution.

## Technologies Used

* Apache Spark
* PySpark
* Databricks
* Python

## Assignment Topics

The assignment includes solutions for the following questions:

1. Roles of Driver, Cluster Manager, and Executor.
2. Spark Lazy Evaluation.
3. Reading a CSV file using Spark.
4. Difference between CSV and Parquet.
5. Selecting specific columns using DataFrame operations.
6. Renaming columns and casting data types.
7. Spark Lineage Graph (DAG) and fault tolerance.
8. Filtering data using multiple conditions.
9. Predicate Pushdown in Parquet.
10. Adding a new calculated column.
11. Difference between Transformations and Actions.
12. Reading Parquet, filtering data, and writing to CSV.
13. Client Mode vs Cluster Mode.
14. Filtering data using OR conditions.
15. Difference between `.show()` and `.collect()` for large datasets.

## Dataset

The assignment uses a sample dataset containing the following columns:

* product_id
* price
* category
* status
* amount
* region
* priority
* user_id
* old_name
* base_price
* order_date

## Learning Outcomes

After completing this assignment, I gained practical experience with:

* Spark Architecture
* DataFrame API
* Reading and writing different file formats
* Filtering and selecting data
* Column transformations
* Data type conversion
* Fault tolerance using DAG
* Predicate Pushdown optimization
* Transformations and Actions
* Client and Cluster deployment modes

## Repository Structure

```text
.
├── Spark_intro.ipynb      # Databricks notebook
├── dataset.csv                 # Sample dataset
└── README.md                   # Project documentation
```

## How to Run

1. Open Databricks.
2. Create or open a notebook.
3. Upload the dataset.
4. Execute the PySpark code for each question.
5. Verify the output.
