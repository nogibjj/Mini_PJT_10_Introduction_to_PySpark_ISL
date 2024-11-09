"""
library functions
"""
import os
import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col

# from pyspark.sql.types import(
#      StructType, 
#      StructField, 
#      IntegerType, 
#      StringType, 
#      DateType)

LOG_FILE = "pyspark_output.md"

def reset_log(): # delete duplicated log
    """Clears the log file at the beginning of each run."""
    with open(LOG_FILE, "w") as file:
        file.write("# PySpark Operation Logs\n\n")


def log_output(operation, output, query=None):
    """adds to a markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"The operation is {operation}\n\n")
        if query: 
            file.write(f"The query is {query}\n\n")
        file.write("The truncated output is: \n\n")
        file.write(output)
        file.write("\n\n")


def start_spark(appName):
    spark = SparkSession.builder.appName(appName).getOrCreate()
    return spark

def end_spark(spark):
    spark.stop()
    return "stopped spark session"

def extract(
    url="https://raw.githubusercontent.com/nogibjj/Mini_PJT_10_Introduction_to_PySpark_ISL/refs/heads/main/Data/HR_Analytics.csv",
    file_path="Data/HR_Analytics.csv",
    directory="Data",
):
    """Extract a URL to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path


def load_data(spark, data="Data/HR_1.csv", name="HR_Attrition"):
    """Load entire CSV and then select required columns"""
    df = spark.read.option("header", "true") \
                   .csv(data)
    df = df.select("EmployeeNumber", "Age", "Attrition", "Department", 
                   "Education", "EducationField", "EmployeeCount")
    log_output("load data", df.limit(10).toPandas().to_markdown())
    return df


def query(spark, df, query, name): 
    """queries using spark sql"""
    df = df.createOrReplaceTempView(name)

    log_output("query data", spark.sql(query).toPandas().to_markdown(), query)

    return spark.sql(query).show()

def describe(df):
    summary_stats_str = df.describe().toPandas().to_markdown()
    log_output("describe data", summary_stats_str)

    return df.describe().show()

def example_transform(df):
    """Transforms the HR_Attrition dataset by adding Attrition_Flag, 
    Department_Code, and EducationField_Code columns."""
    
    df = df.withColumn(
        "Attrition_Flag",
        when(col("Attrition") == "Yes", 1)
        .when(col("Attrition") == "No", 0)
        .otherwise(None)
    )

    df = df.withColumn(
        "Department_Code",
        when(col("Department") == "Sales", 1)
        .when(col("Department") == "Research & Development", 2)
        .when(col("Department") == "Human Resources", 3)
        .otherwise(4)
    )
    
    df = df.withColumn(
       "EducationField_Code",
        when(col("EducationField") == "Life Sciences", 1)
        .when(col("EducationField") == "Marketing", 2)
        .when(col("EducationField") == "Medical", 3)
        .when(col("EducationField") == "Technical Degree", 4)
        .when(col("EducationField") == "Other", 5)
        .otherwise(0)
    )

    log_output("transform data", df.limit(10).toPandas().to_markdown())

###


    return df.show()
