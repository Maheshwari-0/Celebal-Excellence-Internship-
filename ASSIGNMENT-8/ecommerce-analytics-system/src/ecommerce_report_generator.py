import sqlite3
from datetime import datetime, timedelta


def get_previous_period(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    days = (end - start).days + 1
    prev_end = start - timedelta(days=1)
    prev_start = prev_end - timedelta(days=days - 1)
    return prev_start.strftime("%Y-%m-%d"), prev_end.strftime("%Y-%m-%d")

def get_summary(cursor, start_date, end_date):
    query = """
    SELECT
    COUNT(DISTINCT o.order_id),
    IFNULL(SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)),0),
    COUNT(DISTINCT o.customer_id)
    FROM orders o
    JOIN order_items oi
    ON o.order_id = oi.order_id
    WHERE DATE(o.order_date) BETWEEN ? AND ?;"""
    cursor.execute(query, (start_date, end_date))
    return cursor.fetchone()


def get_top_products(cursor, start_date, end_date):
    query = """
    SELECT
    p.product_name,
    SUM(oi.quantity) AS total_quantity
    FROM orders o
    JOIN order_items oi
    ON o.order_id = oi.order_id
    JOIN products p
    ON oi.product_id = p.product_id
    WHERE DATE(o.order_date) BETWEEN ? AND ?
    GROUP BY p.product_name
    ORDER BY total_quantity DESC
    LIMIT 3;"""
    cursor.execute(query, (start_date, end_date))
    return cursor.fetchall()

def percent_change(current, previous):
    if previous == 0:
        return "N/A"
    change = ((current - previous) / previous) * 100
    return f"{change:.2f}%"

def generate_report():
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()
    print("\n E-Commerce Report Generator")
    report_type = input("Enter report type (daily/weekly/monthly): ").lower()
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    current_orders, current_revenue, current_customers = get_summary(
    cursor,
    start_date,
    end_date
    )
    previous_start, previous_end = get_previous_period(
        start_date,
        end_date)
    prev_orders, prev_revenue, prev_customers = get_summary(
    cursor,
    previous_start,
    previous_end
    )
    top_products = get_top_products(
        cursor,
        start_date,
        end_date)
    print("\n REPORT")
    print("Report Type :", report_type)
    print("Date Range  :", start_date, "to", end_date)

    print("\nSummary")
    print("Total Orders     :", current_orders)
    print("Revenue          : {:.2f}".format(current_revenue))
    print("Unique Customers :", current_customers)

    print("\nTop 3 Products")
    for product, qty in top_products:
        print(product, "-", qty)

    print("\nComparison With Previous Period")
    print("Orders Change    :", percent_change(current_orders, prev_orders))
    print("Revenue Change   :", percent_change(current_revenue, prev_revenue))
    print("Customer Change  :", percent_change(current_customers, prev_customers))

    conn.close()


if __name__ == "__main__":
    generate_report()