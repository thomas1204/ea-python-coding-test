import pytest
from contants.models import OrderHistory
from pydantic import ValidationError
from db.repository import get_order_histroy_of_customer

customers = [7888, 15399, 13734]


@pytest.mark.parametrize("customer", customers)
def test_customer_order_history(customer):
    order_histories = get_order_histroy_of_customer(customer)
    model_fields = set(OrderHistory.model_fields.keys())

    assert len(order_histories) > 0

    for oh in order_histories:
        oh_keys = set(oh.keys())
        assert oh_keys == model_fields
