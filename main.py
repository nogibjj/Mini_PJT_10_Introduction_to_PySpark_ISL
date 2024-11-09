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
    reset_log,  # reset_log
)


def main():
    reset_log()  # Clear log at the beginning to avoid duplication

    extract()

    spark = start_spark("HR_Attrition")

    df = load_data(spark)
    describe(df)

    run_query(spark, df, "Yes")
    run_query(spark, df, "No")

    example_transform(df)
    end_spark(spark)


def run_query(spark, df, attrition_value):
    """Filter by Attrition value and log the results."""

    df.createOrReplaceTempView("HR_Attrition")

    query = f"SELECT * FROM HR_Attrition WHERE Attrition = '{attrition_value}'"
    result = spark.sql(query)

    log_output(
        f"Results for Attrition = '{attrition_value}'",
        result.toPandas().to_markdown(),
        query,
    )
    result.show(truncate=False)


if __name__ == "__main__":
    main()
