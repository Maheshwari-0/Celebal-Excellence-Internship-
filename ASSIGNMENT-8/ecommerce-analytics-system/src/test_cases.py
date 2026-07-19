import sqlite3

def test_invalid_order_id():
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()
    print("\nTest 1: order_id not present in orders")
    try:
        cursor.execute("""
        INSERT INTO order_items(order_item_id,order_id,product_id,quantity,unit_price,discount_percent)
        VALUES(999999,999999,1,2,500,10)
        """)
        conn.commit()
        print("Inserted successfully.")
        print("Foreign key constraint is not enforced.")

    except sqlite3.IntegrityError:
        print("Foreign key constraint works correctly.")
    conn.close()


def test_discount_greater_than_100():
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()
    print("\nTest 2: discount_percent > 100")
    revenue = 2 * 500 * (1 - 150 / 100)
    print("Revenue calculated:", revenue)
    if revenue < 0:
        print("Invalid discount. Revenue becomes negative.")
    else:
        print("Discount handled correctly.")
    conn.close()

def test_quantity_zero():
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()
    print("\nTest 3: quantity = 0")
    revenue = 0 * 500 * (1 - 10 / 100)
    print("Revenue:", revenue)
    if revenue == 0:
        print("Zero quantity produces zero revenue.")
    else:
        print("Unexpected result.")
    conn.close()


def test_future_order_date():
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()
    print("\nTest 4: Future order date")
    cursor.execute("""
    SELECT COUNT(*)
    FROM orders
    WHERE DATE(order_date) > DATE('now')""")
    future_orders = cursor.fetchone()[0]
    print("Future orders found:", future_orders)
    if future_orders > 0:
        print("Future dates exist in dataset.")
    else:
        print("No future dates found.")
    conn.close()
if __name__ == "__main__":
    test_invalid_order_id()
    test_discount_greater_than_100()
    test_quantity_zero()
    test_future_order_date()