from db.repository import fetch_customers_with_multiple_orders


def test_customers_with_multiple_orders():
    orders = fetch_customers_with_multiple_orders()
    for o in orders:
        assert o['order_count'] >= 2
