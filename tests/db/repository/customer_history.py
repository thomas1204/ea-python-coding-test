from typing import List
from db import get_connection
from contants.models import OrderHistory


def get_order_histroy_of_customer(customerId: int) -> List[OrderHistory]:
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "select c.firstname || '_' || c.lastname AS cust_fullname, ch.prod_id, p.title, p.price from cust_hist ch left join customers c on c.customerid = ch.customerid left join products p on p.prod_id = ch.prod_id where ch.customerid = %s",
            (customerId,),
        )
        return cursor.fetchall()

    except Exception as e:
        print(f"Error fetching customer order history: {e}")

    finally:
        cursor.close()
        conn.close()
