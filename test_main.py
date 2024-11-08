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
    assert os.path.exists(file_path) is True


def test_load_data(spark):
    """Test loading data into Spark DataFrame"""
    df = load_data(spark)
    assert df is not None
    assert df.count() > 0  # Check if DataFrame is not empty


def test_describe(spark):
    """Test generating statistical summary of data"""
    df = load_data(spark)
    result = describe(df)
    # The describe function usually does not return any value, so we check if it runs without error
    assert result is None or isinstance(result, None.__class__)  # Ensure it returns None or has no output


def test_query(spark):
    """Test querying records where Attrition is 'Yes' and 'No' separately"""
    df = load_data(spark)
    
    # Execute the query function, which runs Attrition 'Yes' and 'No' queries separately
    query(spark, df)
    # If the function doesn't return anything, we can just check that it runs without errors


def test_example_transform(spark):
    """Test data transformation for added columns"""
    df = load_data(spark)
    result = example_transform(df)
    assert result is not None
    assert "Attrition_Flag" in result.columns  # Check if the transformed column exists
    assert "Department_Code" in result.columns
    assert "EducationField_Code" in result.columns


if __name__ == "__main__":
    test_extract()
    spark_session = spark()
    test_load_data(spark_session)
    test_describe(spark_session)
    test_query(spark_session)
    test_example_transform(spark_session)
