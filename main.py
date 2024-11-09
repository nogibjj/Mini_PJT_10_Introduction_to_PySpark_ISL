"""
Main entry point for HR_Attrition analysis
"""

from mylib.lib import (
    start_spark,
    end_spark,
    extract,
    load_data,
    describe,
    example_transform,
    log_output,
)

def main():
    extract()  # Download data file

    spark = start_spark("HR_Attrition")  # Start Spark session

    df = load_data(spark)  # Load data into a DataFrame

    describe(df)  # Show summary statistics

    # Run and log queries for Attrition 'Yes' and 'No' values separately
    run_query(spark, df, "Yes")
    run_query(spark, df, "No")

    example_transform(df)  # Transform data and add new columns

    end_spark(spark)  # Stop Spark session


def run_query(spark, df, attrition_value):
    """Filter by Attrition value and log the results."""
    # Create a temporary SQL view
    df.createOrReplaceTempView("HR_Attrition")

    # Run SQL query for the given Attrition value
    query = f"SELECT * FROM HR_Attrition WHERE Attrition = '{attrition_value}'"
    result = spark.sql(query)

    # Log and print the results
    log_output(
        f"Results for Attrition = '{attrition_value}'",
        result.toPandas().to_markdown(),
        query,
    )
    result.show(truncate=False)


if __name__ == "__main__":
    main()
