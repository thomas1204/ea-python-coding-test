from typing import Optional
from db import get_connection
from contants.models import Customer


def create_customer(customer: Customer):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        print(f"Creating customer {customer}...")
        cursor.execute(
            "SELECT new_customer(%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s, %s, %s, %s, %s);",
            (
                customer.firstname,
                customer.lastname,
                customer.address1,
                customer.address2,
                customer.city,
                customer.state,
                customer.zip,
                customer.country,
                customer.region,
                customer.email,
                customer.phone,
                customer.creditcardtype,
                customer.creditcard,
                customer.creditcardexpiration,
                customer.username,
                customer.password,
                customer.age,
                customer.income,
                customer.gender,
            ),
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error creating customer: {e}")

    finally:
        cursor.close()
        conn.close()


def get_customer(email: str) -> Optional[Customer]:
    conn = get_connection()
    cursor = conn.cursor()
    try:
        print(f"fetching customer {email}...")
        cursor.execute("SELECT * FROM customers WHERE email = %s", (email,))
        row = cursor.fetchone()
        if row is None:
            return None

        return Customer(
            firstname=row["firstname"],
            lastname=row["lastname"],
            address1=row["address1"],
            address2=row["address2"],
            city=row["city"],
            state=row["state"],
            zip=row["zip"],
            country=row["country"],
            region=row["region"],
            email=row["email"],
            phone=row["phone"],
            creditcardtype=row["creditcardtype"],
            creditcard=row["creditcard"],
            creditcardexpiration=row["creditcardexpiration"],
            username=row["username"],
            password=row["password"],
            age=row["age"],
            income=row["income"],
            gender=row["gender"],
        )

    except Exception as e:
        print(f"Error fetching customer: {e}")

    finally:
        cursor.close()
        conn.close()
