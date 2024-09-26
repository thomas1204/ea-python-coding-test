import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
from db.repository import get_all_customer


def load_test_csv():
    df_csv = pd.read_csv(
        "https://eacp.energyaustralia.com.au/codingtest/static/cust-test.csv"
    )
    return df_csv


def normalize_dataframes(df_db, df_csv):
    df_csv = df_csv[df_db.columns]
    for col in df_db.columns:
        if df_db[col].dtype != df_csv[col].dtype:
            df_db[col] = df_db[col].astype(str)
            df_csv[col] = df_csv[col].astype(str)
    return df_db, df_csv


def compare_rows(db_row, csv_row):
    if not db_row.equals(csv_row):
        return (db_row.name, db_row, csv_row)
    return None


def print_mismatch(mismatch):
    email, db_row, csv_row = mismatch
    print(f"Mismatch for email {email}:")
    print(f"DB: {db_row}")
    print(f"CSV: {csv_row}\n")


def compare_rows_by_email(df_db, df_csv):
    mismatches = []
    missing_rows_in_csv = []
    missing_rows_in_db = []

    print(f"S> DB:\n {df_db}\n")
    print(f"S> CSV:\n {df_csv}\n")

    # Set email as the key for both DataFrames
    df_db.set_index("email", inplace=True)
    df_csv.set_index("email", inplace=True)

    # Find emails present in the database but not in the CSV
    missing_in_csv = df_db.index.difference(df_csv.index)
    if not missing_in_csv.empty:
        missing_rows_in_csv = df_db.loc[missing_in_csv]
        print(f"\n=== Missing Rows in CSV ===\n{missing_rows_in_csv}")

    # Find emails present in the CSV but not in the database
    missing_in_db = df_csv.index.difference(df_db.index)
    if not missing_in_db.empty and not missing_in_db.isna().any():
        missing_rows_in_db = df_csv.loc[missing_in_db]
        print(f"\n=== Missing Rows in DB ===\n{missing_rows_in_db}")

    # Compare rows for emails that are common in both datasets
    common_emails = df_db.index.intersection(df_csv.index)

    mismatches = df_db.loc[common_emails].apply(
        lambda db_row: compare_rows(db_row, df_csv.loc[db_row.name]), axis=1
    )
    mismatches = mismatches.dropna().tolist()

    return mismatches, missing_rows_in_csv, missing_rows_in_db


def test_compare_customers_data():
    customers = get_all_customer()
    df_db = pd.DataFrame(customers)
    df_csv = load_test_csv()

    df_db, df_csv = normalize_dataframes(df_db, df_csv)

    mismatches, missing_rows_in_csv, missing_rows_in_db = compare_rows_by_email(
        df_db, df_csv
    )

    # Report mismatched rows
    if mismatches:
        pd.Series(mismatches).apply(print_mismatch)

    # Report missing rows in CSV
    if not missing_rows_in_csv.empty:
        print(f"\n=== Missing Rows in CSV ===\n{missing_rows_in_csv}")

    # Report missing rows in DB
    if len(missing_rows_in_db) > 0:
        print(f"\n=== Missing Rows in DB ===\n{missing_rows_in_db}")

    # Assertions
    assert not mismatches, f"Found {len(mismatches)} mismatched rows."
    assert (
        missing_rows_in_csv.empty
    ), f"Found {len(missing_rows_in_csv)} missing rows in CSV."
    assert (
        missing_rows_in_db.empty
    ), f"Found {len(missing_rows_in_db)} missing rows in DB."


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    report = terminalreporter.getreports("failed")
    if report:
        print(f"\n{len(report)} Test(s) Failed. See details above.")
    else:
        print("\nAll tests passed successfully.")
