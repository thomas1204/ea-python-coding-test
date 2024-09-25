from typing import List
from db import get_connection


def fetch_customers_with_multiple_orders():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "select c.firstname || '_' || c.lastname AS cust_fullname, COUNT(o.orderid) AS order_count from customers c join orders o on c.customerid = o.customerid group by c.customerid having COUNT(o.orderid) > 2"
        )
        return cursor.fetchall()

    except Exception as e:
        print(f"Error fetching customers with multiple orders: {e}")

    finally:
        cursor.close()
        conn.close()
