import pytest
import pandas as pd
import great_expectations as ge
from expectations import define_expectations

CSV_FILE_PATH = "https://eacp.energyaustralia.com.au/codingtest/static/cust-test.csv"


def test_validate_csv():
    validations = define_expectations(CSV_FILE_PATH)
    print(validations)
    assert validations["success"] is True
