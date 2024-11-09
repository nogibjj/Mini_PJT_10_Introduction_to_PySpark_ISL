# IDS-706 Data Engineering Assignment
## Mini Project 10 : Introduction_to_PySpark

#### Status(CI/CD) badge 
[![CICD](https://github.com/nogibjj/Mini_PJT_10_Introduction_to_PySpark/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Mini_PJT_10_Introduction_to_PySpark/actions/workflows/cicd.yml)

---------
### Proejct Purpose

- This project uses PySpark to process a large dataset, focusing on running Spark SQL queries and performing data transformations. I am working with IBM's employee attrition dataset for these tasks.

-----

### Requirements

* ***Use PySpark to perform data processing on a large dataset***
* ***Include at least one Spark SQL query and on data transformation***

### Deliverables

* ***PySpark script***
* ***OUtput data or summaruy report(PDF or markdown)***

--------

### Preperation
* Run 'Codespaces'  
* Setup 'Pyspark' operation environment
* Dataset :[Employee Attrition data](Data/HR_1.csv) provided by IBM

### Process

* `extract` : Downloads the dataset from the specified URL 
* `start_spark` : Initiate a Spark session
* `load_data` : Load the dataset from a CSV file into Spark Data Frame, Selecting only 7 of the 36 columns and creating sample data
* `describe` : Generates descriptive statistice(e.g: Count, Mean)
* `query` : Operates SQL query on the dataset using Spark SQL, based on Attrition values ('Yes', 'No')
* `example_transform` : transforms the dataset by indexing categorical variables as intergers


### Console log file
* [PySpark Output File](pyspark_output.md)

### Remarks
* Both `lib.py` and `main.py` generated logs. However, because the same process was repeated in `main.py`, this caused partial duplication in the log. To address this, `main.py`, deleted previous and rewrite the log.
