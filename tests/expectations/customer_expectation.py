import great_expectations as gx
import pandas as pd
from great_expectations.core.batch import BatchRequest


def define_expectations(csv_file_path: str):
    context = gx.get_context()
    df = pd.read_csv(csv_file_path)

    data_source = context.data_sources.add_pandas("pandas")
    data_asset = data_source.add_dataframe_asset(name="pd dataframe asset")

    batch_definition = data_asset.add_batch_definition_whole_dataframe(
        "batch definition"
    )
    batch = batch_definition.get_batch(batch_parameters={"dataframe": df})

    suite_name = "customer_suite"
    suite = gx.ExpectationSuite(name=suite_name)
    suite = context.suites.add(suite)

    # firstname
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToNotBeNull(column="firstname")
    )
    suite.add_expectation(
        gx.expectations.ExpectColumnValueLengthsToBeBetween(
            column="firstname", min_value=1, max_value=75
        )
    )
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToMatchRegex(
            column="firstname", regex="^[A-Za-z]+$"
        )
    )

    # lastname
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToNotBeNull(column="lastname")
    )
    suite.add_expectation(
        gx.expectations.ExpectColumnValueLengthsToBeBetween(
            column="lastname", min_value=1, max_value=75
        )
    )
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToMatchRegex(
            column="lastname", regex="^[A-Za-z]+$"
        )
    )

    # address1
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToNotBeNull(column="address1")
    )
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeOfType(column="address1", type_="str")
    )
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToMatchRegex(
            column="lastname", regex="^[A-Za-z]+$"
        )
    )

    # city
    suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="city"))
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeOfType(column="city", type_="str")
    )
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToMatchRegex(column="city", regex="^[A-Z]+$")
    )

    # state
    suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="state"))
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeOfType(column="state", type_="str")
    )
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToMatchRegex(column="state", regex="^[A-Z]+$")
    )

    # state
    suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="zip"))
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeOfType(column="zip", type_="int")
    )

    # country
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToNotBeNull(column="country")
    )
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeOfType(column="country", type_="str")
    )
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToMatchRegex(column="country", regex="^US$")
    )

    # email
    suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="email"))
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeOfType(column="email", type_="str")
    )
    suite.add_expectation(gx.expectations.ExpectColumnValuesToBeUnique(column="email"))

    # username
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToNotBeNull(column="username")
    )
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeOfType(column="username", type_="str")
    )
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeUnique(column="username")
    )

    return batch.validate(suite)
