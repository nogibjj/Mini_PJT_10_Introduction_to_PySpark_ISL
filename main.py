"""
Main CLI or app entry point
"""

from mylib.lib import (
    start_spark,
    end_spark,
    extract,
    load_data,
    describe,
    query,
    example_transform,
    log_output
)

def main():
    # extract data
    extract()
    
    # start spark session
    spark = start_spark("HR_Attrition")
    
    # load data into dataframe
    df = load_data(spark)
    
    # example metrics
    describe(df)
    
    # Run queries
    query(spark, df)  
    
    # example transform
    example_transform(df)
    
    # end spark session
    end_spark(spark)

def query(spark, df):
    """Run separate queries to get records where Attrition is 'Yes' and 'No' and log the results."""

    # Temporary view creation for SQL queries
    df.createOrReplaceTempView("HR_Attrition")

    # Query 1: Select rows where Attrition is 'Yes'
    query_yes = """
    SELECT * 
    FROM HR_Attrition 
    WHERE Attrition = 'Yes'
    """
    
    # Query 2: Select rows where Attrition is 'No'
    query_no = """
    SELECT * 
    FROM HR_Attrition 
    WHERE Attrition = 'No'
    """

    # Execute the query for Attrition = 'Yes'
    result_yes = spark.sql(query_yes)
    result_yes_pd = result_yes.limit(10).toPandas()  # Limit to 10 rows for logging
    log_output("Attrition = Yes records", result_yes_pd.to_markdown(), query_yes)
    
    # Show the result in the console for Attrition = 'Yes'
    print("Records with Attrition = 'Yes'")
    result_yes.show()

    # Execute the query for Attrition = 'No'
    result_no = spark.sql(query_no)
    result_no_pd = result_no.limit(10).toPandas()  # Limit to 10 rows for logging
    log_output("Attrition = No records", result_no_pd.to_markdown(), query_no)
    
    # Show the result in the console for Attrition = 'No'
    print("Records with Attrition = 'No'")
    result_no.show()


if __name__ == "__main__":
    main()
