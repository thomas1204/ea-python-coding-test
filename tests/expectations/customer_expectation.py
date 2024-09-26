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
        gx.expectations.ExpectColumnValuesToBeOfType(column="address1", type_="STRING")
    )
    # suite.add_expectation(
    #     gx.expectations.ExpectColumnValuesToMatchRegex(
    #         column="lastname", regex="^[A-Za-z]+$"
    #     )
    # )

    return batch.validate(suite)

    # firstname
    # validator.expectations.ExpectColumnValuesToNotBeNull(column="firstname")
    # gx.expectations.ExpectColumnValueLengthsToBeBetween(
    #     "firstname", min_value=1, max_value=75
    # )
    # df.expect_column_values_to_match_regex("firstname", r"^[A-Za-z]+$")

    # # lastname
    # df.expect_column_values_to_not_be_null("lastname")
    # df.expect_column_value_lengths_to_be_between("lastname", min_value=1, max_value=75)
    # df.expect_column_values_to_match_regex("lastname", r"^[A-Za-z]+$")

    # # address1
    # df.expect_column_values_to_not_be_null("address1")
    # df.expect_column_values_to_be_of_type("address1", "str")
    # df.expect_column_values_to_match_regex(
    #     "address1", r"^\d+\s[A-Za-z\s]+(?:\s[A-Za-z\s]+)?$"
    # )

    # # city
    # df.expect_column_values_to_not_be_null("city")
    # df.expect_column_values_to_be_of_type("city", "str")
    # df.expect_column_values_to_match_regex("city", r"^[A-Z]+$")

    # # state
    # df.expect_column_values_to_not_be_null("state")
    # df.expect_column_values_to_be_of_type("state", "str")
    # df.expect_column_values_to_match_regex("state", r"^[A-Z]+$")
    # df.expect_column_values_to_match_regex("state", r"^.{1,2}$")

    # # zip
    # df.expect_column_values_to_not_be_null("zip")
    # df.expect_column_values_to_be_of_type("zip", "int")

    # # country
    # df.expect_column_values_to_not_be_null("country")
    # df.expect_column_values_to_be_of_type("country", "str")
    # df.expect_column_values_to_match_regex("country_code", r"^US$")

    # # email
    # df.expect_column_values_to_not_be_null("email")
    # df.expect_column_values_to_match_regex("email", r"^[^@]+@[^@]+\.[^@]+$")
    # df.expect_column_values_to_be_unique("email")

    # # Expectations for 'phone'
    # df.expect_column_values_to_not_be_null("phone")
    # df.expect_column_values_to_be_of_type("creditcardtype", "str")
    # df.expect_column_values_to_match_regex("phone", r"^\+?[1-9]\d{1,14}$")

    # # Expectations for 'username'
    # df.expect_column_values_to_not_be_null("username")
    # df.expect_column_values_to_be_unique("username")
    # df.expect_column_value_lengths_to_be_between("username", min_value=3, max_value=20)

    # # Expectations for 'password'
    # df.expect_column_value_lengths_to_be_between("password", min_value=8)

    # # Expectations for 'age'
    # df.expect_column_values_to_be_between("age", 18, 100)

    # # Expectations for 'gender'
    # df.expect_column_values_to_be_in_set(
    #     "gender", ["Male", "Female", "Other", "Prefer not to say"]
    # )

    # # Expectations for 'zip'
    # df.expect_column_values_to_not_be_null("zip")
    # df.expect_column_values_to_be_of_type("zip", "int")

    # # More expectations for other columns as described earlier...

    # return df
