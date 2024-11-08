The operation is load data

The truncated output is: 

|    |   EmployeeNumber |   Age | Attrition   | Department             |   Education | EducationField   |   EmployeeCount |
|---:|-----------------:|------:|:------------|:-----------------------|------------:|:-----------------|----------------:|
|  0 |                1 |    41 | Yes         | Sales                  |           2 | Life Sciences    |               1 |
|  1 |                2 |    49 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  2 |                4 |    37 | Yes         | Research & Development |           2 | Other            |               1 |
|  3 |                5 |    33 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  4 |                7 |    27 | No          | Research & Development |           1 | Medical          |               1 |
|  5 |                8 |    32 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  6 |               10 |    59 | No          | Research & Development |           3 | Medical          |               1 |
|  7 |               11 |    30 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  8 |               12 |    38 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  9 |               13 |    36 | No          | Research & Development |           3 | Medical          |               1 |

The operation is describe data

The truncated output is: 

|    | summary   |   EmployeeNumber |        Age | Attrition   | Department      |   Education | EducationField   |   EmployeeCount |
|---:|:----------|-----------------:|-----------:|:------------|:----------------|------------:|:-----------------|----------------:|
|  0 | count     |         1470     | 1470       | 1470        | 1470            |  1470       | 1470             |            1470 |
|  1 | mean      |         1024.87  |   36.9238  |             |                 |     2.91293 |                  |               1 |
|  2 | stddev    |          602.024 |    9.13537 |             |                 |     1.02416 |                  |               0 |
|  3 | min       |            1     |   18       | No          | Human Resources |     1       | Human Resources  |               1 |
|  4 | max       |          999     |   60       | Yes         | Sales           |     5       | Technical Degree |               1 |

The operation is Attrition = Yes records

The query is 
    SELECT * 
    FROM HR_Attrition 
    WHERE Attrition = 'Yes'
    

The truncated output is: 

|    |   EmployeeNumber |   Age | Attrition   | Department             |   Education | EducationField   |   EmployeeCount |
|---:|-----------------:|------:|:------------|:-----------------------|------------:|:-----------------|----------------:|
|  0 |                1 |    41 | Yes         | Sales                  |           2 | Life Sciences    |               1 |
|  1 |                4 |    37 | Yes         | Research & Development |           2 | Other            |               1 |
|  2 |               19 |    28 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
|  3 |               27 |    36 | Yes         | Sales                  |           4 | Life Sciences    |               1 |
|  4 |               31 |    34 | Yes         | Research & Development |           1 | Medical          |               1 |
|  5 |               33 |    32 | Yes         | Research & Development |           1 | Life Sciences    |               1 |
|  6 |               42 |    39 | Yes         | Sales                  |           3 | Technical Degree |               1 |
|  7 |               45 |    24 | Yes         | Research & Development |           3 | Medical          |               1 |
|  8 |               47 |    50 | Yes         | Sales                  |           2 | Marketing        |               1 |
|  9 |               55 |    26 | Yes         | Research & Development |           3 | Life Sciences    |               1 |

The operation is Attrition = No records

The query is 
    SELECT * 
    FROM HR_Attrition 
    WHERE Attrition = 'No'
    

The truncated output is: 

|    |   EmployeeNumber |   Age | Attrition   | Department             |   Education | EducationField   |   EmployeeCount |
|---:|-----------------:|------:|:------------|:-----------------------|------------:|:-----------------|----------------:|
|  0 |                2 |    49 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  1 |                5 |    33 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  2 |                7 |    27 | No          | Research & Development |           1 | Medical          |               1 |
|  3 |                8 |    32 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  4 |               10 |    59 | No          | Research & Development |           3 | Medical          |               1 |
|  5 |               11 |    30 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  6 |               12 |    38 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  7 |               13 |    36 | No          | Research & Development |           3 | Medical          |               1 |
|  8 |               14 |    35 | No          | Research & Development |           3 | Medical          |               1 |
|  9 |               15 |    29 | No          | Research & Development |           2 | Life Sciences    |               1 |

The operation is transform data

The truncated output is: 

|    |   EmployeeNumber |   Age | Attrition   | Department             |   Education | EducationField   |   EmployeeCount |   Attrition_Flag |   Department_Code |   EducationField_Code |
|---:|-----------------:|------:|:------------|:-----------------------|------------:|:-----------------|----------------:|-----------------:|------------------:|----------------------:|
|  0 |                1 |    41 | Yes         | Sales                  |           2 | Life Sciences    |               1 |                1 |                 1 |                     1 |
|  1 |                2 |    49 | No          | Research & Development |           1 | Life Sciences    |               1 |                0 |                 2 |                     1 |
|  2 |                4 |    37 | Yes         | Research & Development |           2 | Other            |               1 |                1 |                 2 |                     5 |
|  3 |                5 |    33 | No          | Research & Development |           4 | Life Sciences    |               1 |                0 |                 2 |                     1 |
|  4 |                7 |    27 | No          | Research & Development |           1 | Medical          |               1 |                0 |                 2 |                     3 |
|  5 |                8 |    32 | No          | Research & Development |           2 | Life Sciences    |               1 |                0 |                 2 |                     1 |
|  6 |               10 |    59 | No          | Research & Development |           3 | Medical          |               1 |                0 |                 2 |                     3 |
|  7 |               11 |    30 | No          | Research & Development |           1 | Life Sciences    |               1 |                0 |                 2 |                     1 |
|  8 |               12 |    38 | No          | Research & Development |           3 | Life Sciences    |               1 |                0 |                 2 |                     1 |
|  9 |               13 |    36 | No          | Research & Development |           3 | Medical          |               1 |                0 |                 2 |                     3 |

