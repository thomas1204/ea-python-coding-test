import pytest
from faker import Faker
from pydantic import ValidationError
from contants.models import Customer
from db.repository import create_customer, get_customer

fake = Faker()


def generateSampleCustomers():
    customers = []
    for i in range(5):
        customer = Customer(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            email=fake.email(),
            username=fake.user_name(),
            password=fake.password(),
            age=fake.random_int(min=18, max=100),
            phone=fake.phone_number(),
            address1=fake.street_address(),
            address2=fake.building_number(),
            city=fake.city(),
            state=fake.state(),
            country=fake.country_code(),
            zip=fake.zipcode(),
            region=fake.random_int(min=1, max=10),
            creditcardtype=fake.random_int(min=1, max=4),
            creditcard=fake.credit_card_number(),
            creditcardexpiration=fake.credit_card_expire(),
            income=fake.random_int(min=10000, max=1000000),
            gender=fake.random_element(elements=("M", "F")),
        )
        customers.append(customer)
    return customers


@pytest.mark.parametrize("customer", generateSampleCustomers())
def test_insert_customer(customer):
    try:
        create_customer(customer)
        created_customer = get_customer(customer.email)
        assert created_customer is not None
        assert created_customer == customer
    except ValidationError as e:
        pytest.fail(f"Validation failed: {e}")
    except Exception as e:
        pytest.fail(f"Failed to insert/verify customer {customer.email}: {e}")
