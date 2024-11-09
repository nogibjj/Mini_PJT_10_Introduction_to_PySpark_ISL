"""
Test goes here
"""

import os
import pytest
from mylib.lib import (
    extract,
    load_data,
    describe,
    query,
    example_transform,
    start_spark,
    end_spark,
)


@pytest.fixture(scope="module")
def spark():
    """Fixture for initializing and stopping Spark session for tests"""
    spark = start_spark("TestApp")
    yield spark
    end_spark(spark)


def test_extract():
    """Test file extraction from URL"""
    file_path = extract()
    assert os.path.exists(file_path), "Extracted file does not exist."


def test_load_data(spark):
    """Test loading data into Spark DataFrame"""
    df = load_data(spark)
    assert df is not None, "Data loading failed: DataFrame is None."


def test_describe(spark):
    """Test generating statistical summary of data"""
    df = load_data(spark)
    describe(df)  # Expecting only successful execution


def test_query(spark):
    """Test querying records where Attrition is 'Yes' and 'No' separately"""
    df = load_data(spark)
    view_name = "HR_Attrition"

    # Run query for 'Yes' Attrition
    query(
        spark,
        df,
        "SELECT Attrition, COUNT(*) AS attrition_count "
        "FROM HR_Attrition WHERE Attrition = 'Yes' "
        "GROUP BY Attrition",
        view_name,
    )

    # Run query for 'No' Attrition
    query(
        spark,
        df,
        "SELECT Attrition, COUNT(*) AS attrition_count "
        "FROM HR_Attrition WHERE Attrition = 'No' "
        "GROUP BY Attrition",
        view_name,
    )


def test_example_transform(spark):
    """Test that example_transform runs and modifies the DataFrame"""
    df = load_data(spark)
    example_transform(df)  # Expecting only successful execution


if __name__ == "__main__":
    pytest.main()
