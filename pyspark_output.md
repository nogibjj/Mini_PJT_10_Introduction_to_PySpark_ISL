# PySpark Operation Logs

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

The operation is Results for Attrition = 'Yes'

The query is SELECT * FROM HR_Attrition WHERE Attrition = 'Yes'

The truncated output is: 

|     |   EmployeeNumber |   Age | Attrition   | Department             |   Education | EducationField   |   EmployeeCount |
|----:|-----------------:|------:|:------------|:-----------------------|------------:|:-----------------|----------------:|
|   0 |                1 |    41 | Yes         | Sales                  |           2 | Life Sciences    |               1 |
|   1 |                4 |    37 | Yes         | Research & Development |           2 | Other            |               1 |
|   2 |               19 |    28 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
|   3 |               27 |    36 | Yes         | Sales                  |           4 | Life Sciences    |               1 |
|   4 |               31 |    34 | Yes         | Research & Development |           1 | Medical          |               1 |
|   5 |               33 |    32 | Yes         | Research & Development |           1 | Life Sciences    |               1 |
|   6 |               42 |    39 | Yes         | Sales                  |           3 | Technical Degree |               1 |
|   7 |               45 |    24 | Yes         | Research & Development |           3 | Medical          |               1 |
|   8 |               47 |    50 | Yes         | Sales                  |           2 | Marketing        |               1 |
|   9 |               55 |    26 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
|  10 |               58 |    41 | Yes         | Research & Development |           3 | Technical Degree |               1 |
|  11 |               64 |    48 | Yes         | Research & Development |           2 | Life Sciences    |               1 |
|  12 |               65 |    28 | Yes         | Research & Development |           4 | Technical Degree |               1 |
|  13 |               90 |    36 | Yes         | Research & Development |           3 | Medical          |               1 |
|  14 |              118 |    46 | Yes         | Sales                  |           2 | Medical          |               1 |
|  15 |              133 |    37 | Yes         | Human Resources        |           4 | Human Resources  |               1 |
|  16 |              137 |    20 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
|  17 |              142 |    25 | Yes         | Sales                  |           3 | Marketing        |               1 |
|  18 |              147 |    34 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
|  19 |              161 |    56 | Yes         | Research & Development |           4 | Life Sciences    |               1 |
|  20 |              163 |    31 | Yes         | Sales                  |           4 | Life Sciences    |               1 |
|  21 |              165 |    58 | Yes         | Research & Development |           4 | Medical          |               1 |
|  22 |              167 |    19 | Yes         | Sales                  |           1 | Marketing        |               1 |
|  23 |              175 |    31 | Yes         | Sales                  |           3 | Life Sciences    |               1 |
|  24 |              179 |    51 | Yes         | Research & Development |           4 | Life Sciences    |               1 |
|  25 |              190 |    32 | Yes         | Research & Development |           3 | Medical          |               1 |
|  26 |              235 |    19 | Yes         | Sales                  |           1 | Technical Degree |               1 |
|  27 |              243 |    19 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
|  28 |              248 |    41 | Yes         | Sales                  |           2 | Marketing        |               1 |
|  29 |              261 |    35 | Yes         | Research & Development |           2 | Life Sciences    |               1 |
|  30 |              282 |    38 | Yes         | Research & Development |           1 | Medical          |               1 |
|  31 |              283 |    29 | Yes         | Sales                  |           3 | Marketing        |               1 |
|  32 |              291 |    32 | Yes         | Sales                  |           4 | Medical          |               1 |
|  33 |              297 |    30 | Yes         | Research & Development |           3 | Technical Degree |               1 |
|  34 |              299 |    30 | Yes         | Sales                  |           4 | Marketing        |               1 |
|  35 |              300 |    29 | Yes         | Research & Development |           3 | Technical Degree |               1 |
|  36 |              315 |    29 | Yes         | Research & Development |           1 | Medical          |               1 |
|  37 |              325 |    33 | Yes         | Research & Development |           3 | Medical          |               1 |
|  38 |              328 |    33 | Yes         | Research & Development |           2 | Life Sciences    |               1 |
|  39 |              331 |    32 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
|  40 |              342 |    37 | Yes         | Research & Development |           3 | Medical          |               1 |
|  41 |              355 |    31 | Yes         | Research & Development |           2 | Medical          |               1 |
|  42 |              364 |    28 | Yes         | Research & Development |           4 | Life Sciences    |               1 |
|  43 |              376 |    47 | Yes         | Research & Development |           4 | Life Sciences    |               1 |
|  44 |              392 |    44 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
|  45 |              394 |    26 | Yes         | Research & Development |           4 | Medical          |               1 |
|  46 |              401 |    26 | Yes         | Sales                  |           4 | Marketing        |               1 |
|  47 |              405 |    18 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
|  48 |              433 |    52 | Yes         | Research & Development |           4 | Medical          |               1 |
|  49 |              440 |    28 | Yes         | Research & Development |           4 | Medical          |               1 |
|  50 |              445 |    39 | Yes         | Sales                  |           2 | Medical          |               1 |
|  51 |              454 |    29 | Yes         | Research & Development |           4 | Other            |               1 |
|  52 |              478 |    21 | Yes         | Sales                  |           1 | Technical Degree |               1 |
|  53 |              485 |    33 | Yes         | Sales                  |           3 | Marketing        |               1 |
|  54 |              488 |    41 | Yes         | Sales                  |           3 | Marketing        |               1 |
|  55 |              492 |    40 | Yes         | Sales                  |           2 | Marketing        |               1 |
|  56 |              494 |    21 | Yes         | Sales                  |           3 | Life Sciences    |               1 |
|  57 |              502 |    34 | Yes         | Sales                  |           3 | Marketing        |               1 |
|  58 |              510 |    26 | Yes         | Research & Development |           1 | Technical Degree |               1 |
|  59 |              514 |    30 | Yes         | Research & Development |           3 | Technical Degree |               1 |
|  60 |              538 |    25 | Yes         | Research & Development |           3 | Medical          |               1 |
|  61 |              554 |    24 | Yes         | Sales                  |           1 | Technical Degree |               1 |
|  62 |              555 |    34 | Yes         | Sales                  |           2 | Marketing        |               1 |
|  63 |              565 |    29 | Yes         | Research & Development |           5 | Technical Degree |               1 |
|  64 |              566 |    19 | Yes         | Human Resources        |           2 | Technical Degree |               1 |
|  65 |              582 |    33 | Yes         | Research & Development |           1 | Medical          |               1 |
|  66 |              584 |    33 | Yes         | Research & Development |           1 | Medical          |               1 |
|  67 |              587 |    31 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
|  68 |              590 |    34 | Yes         | Human Resources        |           3 | Human Resources  |               1 |
|  69 |              593 |    22 | Yes         | Research & Development |           1 | Technical Degree |               1 |
|  70 |              608 |    26 | Yes         | Human Resources        |           4 | Life Sciences    |               1 |
|  71 |              614 |    18 | Yes         | Sales                  |           3 | Marketing        |               1 |
|  72 |              622 |    26 | Yes         | Research & Development |           3 | Technical Degree |               1 |
|  73 |              631 |    32 | Yes         | Sales                  |           4 | Other            |               1 |
|  74 |              647 |    24 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
|  75 |              648 |    30 | Yes         | Sales                  |           4 | Life Sciences    |               1 |
|  76 |              650 |    31 | Yes         | Sales                  |           4 | Medical          |               1 |
|  77 |              667 |    27 | Yes         | Sales                  |           1 | Marketing        |               1 |
|  78 |              684 |    45 | Yes         | Sales                  |           4 | Life Sciences    |               1 |
|  79 |              701 |    20 | Yes         | Research & Development |           1 | Medical          |               1 |
|  80 |              702 |    33 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
|  81 |              720 |    24 | Yes         | Sales                  |           2 | Life Sciences    |               1 |
|  82 |              723 |    50 | Yes         | Sales                  |           2 | Technical Degree |               1 |
|  83 |              741 |    28 | Yes         | Research & Development |           2 | Life Sciences    |               1 |
|  84 |              752 |    42 | Yes         | Research & Development |           3 | Medical          |               1 |
|  85 |              780 |    33 | Yes         | Research & Development |           4 | Other            |               1 |
|  86 |              785 |    47 | Yes         | Sales                  |           2 | Life Sciences    |               1 |
|  87 |              787 |    55 | Yes         | Research & Development |           3 | Medical          |               1 |
|  88 |              796 |    26 | Yes         | Sales                  |           3 | Technical Degree |               1 |
|  89 |              811 |    23 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
|  90 |              816 |    29 | Yes         | Research & Development |           2 | Life Sciences    |               1 |
|  91 |              819 |    33 | Yes         | Sales                  |           3 | Marketing        |               1 |
|  92 |              825 |    58 | Yes         | Research & Development |           4 | Life Sciences    |               1 |
|  93 |              828 |    28 | Yes         | Research & Development |           4 | Medical          |               1 |
|  94 |              840 |    49 | Yes         | Sales                  |           3 | Marketing        |               1 |
|  95 |              842 |    55 | Yes         | Sales                  |           1 | Medical          |               1 |
|  96 |              848 |    26 | Yes         | Research & Development |           2 | Medical          |               1 |
|  97 |              881 |    35 | Yes         | Research & Development |           4 | Life Sciences    |               1 |
|  98 |              896 |    29 | Yes         | Sales                  |           3 | Medical          |               1 |
|  99 |              911 |    32 | Yes         | Research & Development |           4 | Life Sciences    |               1 |
| 100 |              918 |    58 | Yes         | Research & Development |           1 | Life Sciences    |               1 |
| 101 |              922 |    20 | Yes         | Sales                  |           3 | Medical          |               1 |
| 102 |              923 |    21 | Yes         | Research & Development |           1 | Other            |               1 |
| 103 |              926 |    22 | Yes         | Research & Development |           1 | Life Sciences    |               1 |
| 104 |              927 |    41 | Yes         | Research & Development |           4 | Life Sciences    |               1 |
| 105 |              932 |    39 | Yes         | Research & Development |           3 | Medical          |               1 |
| 106 |              952 |    25 | Yes         | Sales                  |           2 | Marketing        |               1 |
| 107 |              959 |    19 | Yes         | Sales                  |           3 | Other            |               1 |
| 108 |              960 |    20 | Yes         | Research & Development |           3 | Technical Degree |               1 |
| 109 |              967 |    36 | Yes         | Sales                  |           1 | Life Sciences    |               1 |
| 110 |              970 |    37 | Yes         | Sales                  |           4 | Life Sciences    |               1 |
| 111 |              977 |    58 | Yes         | Research & Development |           3 | Technical Degree |               1 |
| 112 |              986 |    40 | Yes         | Sales                  |           3 | Life Sciences    |               1 |
| 113 |              991 |    31 | Yes         | Research & Development |           2 | Medical          |               1 |
| 114 |              994 |    29 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
| 115 |             1004 |    30 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
| 116 |             1010 |    35 | Yes         | Research & Development |           4 | Other            |               1 |
| 117 |             1016 |    20 | Yes         | Research & Development |           3 | Medical          |               1 |
| 118 |             1017 |    30 | Yes         | Research & Development |           3 | Medical          |               1 |
| 119 |             1033 |    37 | Yes         | Research & Development |           2 | Medical          |               1 |
| 120 |             1037 |    26 | Yes         | Sales                  |           2 | Medical          |               1 |
| 121 |             1038 |    52 | Yes         | Sales                  |           1 | Marketing        |               1 |
| 122 |             1042 |    36 | Yes         | Research & Development |           4 | Life Sciences    |               1 |
| 123 |             1052 |    36 | Yes         | Research & Development |           3 | Other            |               1 |
| 124 |             1053 |    26 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
| 125 |             1077 |    20 | Yes         | Sales                  |           3 | Marketing        |               1 |
| 126 |             1079 |    21 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
| 127 |             1081 |    51 | Yes         | Research & Development |           4 | Life Sciences    |               1 |
| 128 |             1082 |    28 | Yes         | Research & Development |           2 | Technical Degree |               1 |
| 129 |             1098 |    44 | Yes         | Human Resources        |           2 | Medical          |               1 |
| 130 |             1100 |    35 | Yes         | Sales                  |           3 | Technical Degree |               1 |
| 131 |             1101 |    33 | Yes         | Research & Development |           4 | Medical          |               1 |
| 132 |             1106 |    25 | Yes         | Research & Development |           1 | Technical Degree |               1 |
| 133 |             1107 |    26 | Yes         | Research & Development |           3 | Medical          |               1 |
| 134 |             1108 |    33 | Yes         | Research & Development |           3 | Medical          |               1 |
| 135 |             1111 |    28 | Yes         | Research & Development |           3 | Medical          |               1 |
| 136 |             1113 |    50 | Yes         | Sales                  |           4 | Other            |               1 |
| 137 |             1127 |    39 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
| 138 |             1156 |    18 | Yes         | Research & Development |           1 | Medical          |               1 |
| 139 |             1157 |    33 | Yes         | Sales                  |           4 | Marketing        |               1 |
| 140 |             1160 |    31 | Yes         | Research & Development |           3 | Medical          |               1 |
| 141 |             1165 |    29 | Yes         | Sales                  |           1 | Life Sciences    |               1 |
| 142 |             1167 |    42 | Yes         | Sales                  |           3 | Life Sciences    |               1 |
| 143 |             1175 |    28 | Yes         | Research & Development |           1 | Life Sciences    |               1 |
| 144 |             1188 |    43 | Yes         | Sales                  |           3 | Marketing        |               1 |
| 145 |             1200 |    44 | Yes         | Research & Development |           4 | Life Sciences    |               1 |
| 146 |             1203 |    22 | Yes         | Research & Development |           4 | Life Sciences    |               1 |
| 147 |             1210 |    41 | Yes         | Research & Development |           2 | Life Sciences    |               1 |
| 148 |             1219 |    24 | Yes         | Research & Development |           2 | Life Sciences    |               1 |
| 149 |             1248 |    19 | Yes         | Research & Development |           3 | Medical          |               1 |
| 150 |             1273 |    25 | Yes         | Sales                  |           1 | Life Sciences    |               1 |
| 151 |             1277 |    45 | Yes         | Sales                  |           3 | Marketing        |               1 |
| 152 |             1279 |    21 | Yes         | Research & Development |           2 | Life Sciences    |               1 |
| 153 |             1295 |    44 | Yes         | Research & Development |           3 | Medical          |               1 |
| 154 |             1299 |    29 | Yes         | Research & Development |           3 | Technical Degree |               1 |
| 155 |             1309 |    32 | Yes         | Research & Development |           2 | Life Sciences    |               1 |
| 156 |             1310 |    39 | Yes         | Research & Development |           3 | Medical          |               1 |
| 157 |             1318 |    40 | Yes         | Sales                  |           4 | Marketing        |               1 |
| 158 |             1319 |    52 | Yes         | Sales                  |           3 | Life Sciences    |               1 |
| 159 |             1331 |    31 | Yes         | Sales                  |           3 | Life Sciences    |               1 |
| 160 |             1333 |    44 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
| 161 |             1360 |    58 | Yes         | Research & Development |           4 | Medical          |               1 |
| 162 |             1372 |    55 | Yes         | Sales                  |           4 | Marketing        |               1 |
| 163 |             1379 |    31 | Yes         | Sales                  |           3 | Life Sciences    |               1 |
| 164 |             1380 |    35 | Yes         | Sales                  |           4 | Marketing        |               1 |
| 165 |             1389 |    31 | Yes         | Research & Development |           4 | Medical          |               1 |
| 166 |             1405 |    27 | Yes         | Research & Development |           4 | Life Sciences    |               1 |
| 167 |             1420 |    49 | Yes         | Research & Development |           2 | Life Sciences    |               1 |
| 168 |             1421 |    29 | Yes         | Research & Development |           1 | Other            |               1 |
| 169 |             1427 |    31 | Yes         | Sales                  |           4 | Life Sciences    |               1 |
| 170 |             1433 |    31 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
| 171 |             1439 |    25 | Yes         | Sales                  |           2 | Life Sciences    |               1 |
| 172 |             1457 |    46 | Yes         | Sales                  |           3 | Marketing        |               1 |
| 173 |             1458 |    39 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
| 174 |             1459 |    31 | Yes         | Research & Development |           5 | Life Sciences    |               1 |
| 175 |             1464 |    31 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
| 176 |             1467 |    34 | Yes         | Human Resources        |           4 | Technical Degree |               1 |
| 177 |             1486 |    28 | Yes         | Sales                  |           3 | Technical Degree |               1 |
| 178 |             1487 |    29 | Yes         | Sales                  |           3 | Technical Degree |               1 |
| 179 |             1489 |    34 | Yes         | Sales                  |           4 | Medical          |               1 |
| 180 |             1494 |    24 | Yes         | Research & Development |           3 | Medical          |               1 |
| 181 |             1504 |    28 | Yes         | Research & Development |           2 | Medical          |               1 |
| 182 |             1522 |    29 | Yes         | Research & Development |           4 | Technical Degree |               1 |
| 183 |             1534 |    40 | Yes         | Research & Development |           4 | Life Sciences    |               1 |
| 184 |             1537 |    31 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
| 185 |             1562 |    30 | Yes         | Sales                  |           3 | Life Sciences    |               1 |
| 186 |             1569 |    35 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
| 187 |             1572 |    53 | Yes         | Research & Development |           5 | Technical Degree |               1 |
| 188 |             1573 |    38 | Yes         | Research & Development |           3 | Medical          |               1 |
| 189 |             1604 |    28 | Yes         | Research & Development |           3 | Medical          |               1 |
| 190 |             1624 |    18 | Yes         | Sales                  |           2 | Medical          |               1 |
| 191 |             1639 |    35 | Yes         | Sales                  |           3 | Medical          |               1 |
| 192 |             1645 |    35 | Yes         | Sales                  |           2 | Medical          |               1 |
| 193 |             1649 |    40 | Yes         | Research & Development |           3 | Life Sciences    |               1 |
| 194 |             1667 |    35 | Yes         | Sales                  |           4 | Other            |               1 |
| 195 |             1684 |    23 | Yes         | Research & Development |           1 | Medical          |               1 |
| 196 |             1691 |    48 | Yes         | Sales                  |           2 | Medical          |               1 |
| 197 |             1692 |    32 | Yes         | Research & Development |           4 | Life Sciences    |               1 |
| 198 |             1702 |    23 | Yes         | Sales                  |           3 | Life Sciences    |               1 |
| 199 |             1714 |    24 | Yes         | Human Resources        |           1 | Human Resources  |               1 |
| 200 |             1716 |    47 | Yes         | Sales                  |           3 | Life Sciences    |               1 |
| 201 |             1733 |    36 | Yes         | Sales                  |           5 | Marketing        |               1 |
| 202 |             1734 |    32 | Yes         | Sales                  |           2 | Life Sciences    |               1 |
| 203 |             1747 |    30 | Yes         | Human Resources        |           3 | Human Resources  |               1 |
| 204 |             1752 |    29 | Yes         | Sales                  |           3 | Marketing        |               1 |
| 205 |             1758 |    33 | Yes         | Sales                  |           3 | Life Sciences    |               1 |
| 206 |             1761 |    31 | Yes         | Sales                  |           4 | Marketing        |               1 |
| 207 |             1767 |    43 | Yes         | Research & Development |           3 | Technical Degree |               1 |
| 208 |             1780 |    21 | Yes         | Sales                  |           1 | Marketing        |               1 |
| 209 |             1783 |    22 | Yes         | Research & Development |           1 | Medical          |               1 |
| 210 |             1792 |    44 | Yes         | Research & Development |           2 | Medical          |               1 |
| 211 |             1797 |    35 | Yes         | Sales                  |           3 | Life Sciences    |               1 |
| 212 |             1807 |    34 | Yes         | Research & Development |           4 | Life Sciences    |               1 |
| 213 |             1809 |    37 | Yes         | Research & Development |           4 | Medical          |               1 |
| 214 |             1818 |    26 | Yes         | Human Resources        |           2 | Medical          |               1 |
| 215 |             1821 |    46 | Yes         | Research & Development |           2 | Medical          |               1 |
| 216 |             1842 |    31 | Yes         | Human Resources        |           5 | Human Resources  |               1 |
| 217 |             1844 |    29 | Yes         | Human Resources        |           3 | Human Resources  |               1 |
| 218 |             1862 |    32 | Yes         | Sales                  |           4 | Marketing        |               1 |
| 219 |             1868 |    29 | Yes         | Research & Development |           2 | Life Sciences    |               1 |
| 220 |             1869 |    46 | Yes         | Sales                  |           3 | Life Sciences    |               1 |
| 221 |             1876 |    30 | Yes         | Sales                  |           3 | Medical          |               1 |
| 222 |             1878 |    22 | Yes         | Research & Development |           1 | Life Sciences    |               1 |
| 223 |             1905 |    34 | Yes         | Research & Development |           4 | Technical Degree |               1 |
| 224 |             1907 |    56 | Yes         | Research & Development |           2 | Life Sciences    |               1 |
| 225 |             1928 |    29 | Yes         | Sales                  |           3 | Technical Degree |               1 |
| 226 |             1933 |    28 | Yes         | Sales                  |           2 | Marketing        |               1 |
| 227 |             1939 |    32 | Yes         | Research & Development |           2 | Life Sciences    |               1 |
| 228 |             1944 |    27 | Yes         | Human Resources        |           3 | Human Resources  |               1 |
| 229 |             1960 |    28 | Yes         | Research & Development |           3 | Technical Degree |               1 |
| 230 |             1967 |    31 | Yes         | Sales                  |           4 | Marketing        |               1 |
| 231 |             1968 |    53 | Yes         | Sales                  |           4 | Life Sciences    |               1 |
| 232 |             2023 |    23 | Yes         | Sales                  |           3 | Marketing        |               1 |
| 233 |             2027 |    29 | Yes         | Research & Development |           4 | Medical          |               1 |
| 234 |             2032 |    56 | Yes         | Research & Development |           2 | Technical Degree |               1 |
| 235 |             2044 |    50 | Yes         | Sales                  |           4 | Life Sciences    |               1 |
| 236 |             2055 |    50 | Yes         | Sales                  |           3 | Marketing        |               1 |

The operation is Results for Attrition = 'No'

The query is SELECT * FROM HR_Attrition WHERE Attrition = 'No'

The truncated output is: 

|      |   EmployeeNumber |   Age | Attrition   | Department             |   Education | EducationField   |   EmployeeCount |
|-----:|-----------------:|------:|:------------|:-----------------------|------------:|:-----------------|----------------:|
|    0 |                2 |    49 | No          | Research & Development |           1 | Life Sciences    |               1 |
|    1 |                5 |    33 | No          | Research & Development |           4 | Life Sciences    |               1 |
|    2 |                7 |    27 | No          | Research & Development |           1 | Medical          |               1 |
|    3 |                8 |    32 | No          | Research & Development |           2 | Life Sciences    |               1 |
|    4 |               10 |    59 | No          | Research & Development |           3 | Medical          |               1 |
|    5 |               11 |    30 | No          | Research & Development |           1 | Life Sciences    |               1 |
|    6 |               12 |    38 | No          | Research & Development |           3 | Life Sciences    |               1 |
|    7 |               13 |    36 | No          | Research & Development |           3 | Medical          |               1 |
|    8 |               14 |    35 | No          | Research & Development |           3 | Medical          |               1 |
|    9 |               15 |    29 | No          | Research & Development |           2 | Life Sciences    |               1 |
|   10 |               16 |    31 | No          | Research & Development |           1 | Life Sciences    |               1 |
|   11 |               18 |    34 | No          | Research & Development |           2 | Medical          |               1 |
|   12 |               20 |    29 | No          | Research & Development |           4 | Life Sciences    |               1 |
|   13 |               21 |    32 | No          | Research & Development |           2 | Life Sciences    |               1 |
|   14 |               22 |    22 | No          | Research & Development |           2 | Medical          |               1 |
|   15 |               23 |    53 | No          | Sales                  |           4 | Life Sciences    |               1 |
|   16 |               24 |    38 | No          | Research & Development |           3 | Life Sciences    |               1 |
|   17 |               26 |    24 | No          | Research & Development |           2 | Other            |               1 |
|   18 |               28 |    34 | No          | Research & Development |           4 | Life Sciences    |               1 |
|   19 |               30 |    21 | No          | Research & Development |           2 | Life Sciences    |               1 |
|   20 |               32 |    53 | No          | Research & Development |           3 | Other            |               1 |
|   21 |               35 |    42 | No          | Sales                  |           4 | Marketing        |               1 |
|   22 |               36 |    44 | No          | Research & Development |           4 | Medical          |               1 |
|   23 |               38 |    46 | No          | Sales                  |           4 | Marketing        |               1 |
|   24 |               39 |    33 | No          | Research & Development |           3 | Medical          |               1 |
|   25 |               40 |    44 | No          | Research & Development |           4 | Other            |               1 |
|   26 |               41 |    30 | No          | Research & Development |           2 | Medical          |               1 |
|   27 |               46 |    43 | No          | Research & Development |           2 | Medical          |               1 |
|   28 |               49 |    35 | No          | Sales                  |           3 | Marketing        |               1 |
|   29 |               51 |    36 | No          | Research & Development |           4 | Life Sciences    |               1 |
|   30 |               52 |    33 | No          | Sales                  |           3 | Life Sciences    |               1 |
|   31 |               53 |    35 | No          | Research & Development |           2 | Other            |               1 |
|   32 |               54 |    27 | No          | Research & Development |           4 | Life Sciences    |               1 |
|   33 |               56 |    27 | No          | Sales                  |           3 | Life Sciences    |               1 |
|   34 |               57 |    30 | No          | Research & Development |           2 | Medical          |               1 |
|   35 |               60 |    34 | No          | Sales                  |           4 | Marketing        |               1 |
|   36 |               61 |    37 | No          | Research & Development |           2 | Life Sciences    |               1 |
|   37 |               62 |    46 | No          | Sales                  |           4 | Marketing        |               1 |
|   38 |               63 |    35 | No          | Research & Development |           1 | Life Sciences    |               1 |
|   39 |               68 |    44 | No          | Sales                  |           5 | Marketing        |               1 |
|   40 |               70 |    35 | No          | Research & Development |           2 | Medical          |               1 |
|   41 |               72 |    26 | No          | Sales                  |           3 | Marketing        |               1 |
|   42 |               73 |    33 | No          | Research & Development |           2 | Life Sciences    |               1 |
|   43 |               74 |    35 | No          | Sales                  |           5 | Life Sciences    |               1 |
|   44 |               75 |    35 | No          | Research & Development |           4 | Medical          |               1 |
|   45 |               76 |    31 | No          | Research & Development |           4 | Life Sciences    |               1 |
|   46 |               77 |    37 | No          | Research & Development |           4 | Life Sciences    |               1 |
|   47 |               78 |    32 | No          | Research & Development |           3 | Medical          |               1 |
|   48 |               79 |    38 | No          | Research & Development |           5 | Life Sciences    |               1 |
|   49 |               80 |    50 | No          | Research & Development |           2 | Medical          |               1 |
|   50 |               81 |    59 | No          | Sales                  |           3 | Life Sciences    |               1 |
|   51 |               83 |    36 | No          | Research & Development |           3 | Technical Degree |               1 |
|   52 |               84 |    55 | No          | Research & Development |           3 | Medical          |               1 |
|   53 |               85 |    36 | No          | Research & Development |           3 | Life Sciences    |               1 |
|   54 |               86 |    45 | No          | Research & Development |           3 | Life Sciences    |               1 |
|   55 |               88 |    35 | No          | Research & Development |           3 | Medical          |               1 |
|   56 |               91 |    59 | No          | Sales                  |           1 | Life Sciences    |               1 |
|   57 |               94 |    29 | No          | Research & Development |           3 | Life Sciences    |               1 |
|   58 |               95 |    31 | No          | Research & Development |           4 | Medical          |               1 |
|   59 |               96 |    32 | No          | Research & Development |           3 | Life Sciences    |               1 |
|   60 |               97 |    36 | No          | Research & Development |           3 | Life Sciences    |               1 |
|   61 |               98 |    31 | No          | Research & Development |           4 | Life Sciences    |               1 |
|   62 |              100 |    35 | No          | Sales                  |           4 | Marketing        |               1 |
|   63 |              101 |    45 | No          | Research & Development |           4 | Other            |               1 |
|   64 |              102 |    37 | No          | Research & Development |           4 | Medical          |               1 |
|   65 |              103 |    46 | No          | Human Resources        |           2 | Medical          |               1 |
|   66 |              104 |    30 | No          | Research & Development |           1 | Life Sciences    |               1 |
|   67 |              105 |    35 | No          | Research & Development |           3 | Medical          |               1 |
|   68 |              106 |    55 | No          | Sales                  |           2 | Life Sciences    |               1 |
|   69 |              107 |    38 | No          | Research & Development |           3 | Medical          |               1 |
|   70 |              110 |    34 | No          | Research & Development |           2 | Medical          |               1 |
|   71 |              112 |    56 | No          | Research & Development |           3 | Life Sciences    |               1 |
|   72 |              113 |    23 | No          | Sales                  |           1 | Technical Degree |               1 |
|   73 |              116 |    51 | No          | Research & Development |           4 | Life Sciences    |               1 |
|   74 |              117 |    30 | No          | Research & Development |           3 | Life Sciences    |               1 |
|   75 |              119 |    40 | No          | Research & Development |           4 | Life Sciences    |               1 |
|   76 |              120 |    51 | No          | Sales                  |           4 | Marketing        |               1 |
|   77 |              121 |    30 | No          | Sales                  |           2 | Medical          |               1 |
|   78 |              124 |    46 | No          | Research & Development |           3 | Medical          |               1 |
|   79 |              125 |    32 | No          | Sales                  |           4 | Medical          |               1 |
|   80 |              126 |    54 | No          | Research & Development |           4 | Technical Degree |               1 |
|   81 |              128 |    24 | No          | Sales                  |           2 | Other            |               1 |
|   82 |              129 |    28 | No          | Sales                  |           3 | Medical          |               1 |
|   83 |              131 |    58 | No          | Sales                  |           4 | Medical          |               1 |
|   84 |              132 |    44 | No          | Research & Development |           3 | Medical          |               1 |
|   85 |              134 |    32 | No          | Research & Development |           1 | Life Sciences    |               1 |
|   86 |              138 |    34 | No          | Research & Development |           4 | Other            |               1 |
|   87 |              139 |    37 | No          | Research & Development |           2 | Life Sciences    |               1 |
|   88 |              140 |    59 | No          | Human Resources        |           4 | Human Resources  |               1 |
|   89 |              141 |    50 | No          | Research & Development |           3 | Life Sciences    |               1 |
|   90 |              143 |    25 | No          | Research & Development |           1 | Medical          |               1 |
|   91 |              144 |    22 | No          | Research & Development |           3 | Medical          |               1 |
|   92 |              145 |    51 | No          | Research & Development |           4 | Medical          |               1 |
|   93 |              148 |    54 | No          | Human Resources        |           3 | Human Resources  |               1 |
|   94 |              150 |    24 | No          | Research & Development |           1 | Life Sciences    |               1 |
|   95 |              151 |    34 | No          | Research & Development |           4 | Life Sciences    |               1 |
|   96 |              152 |    37 | No          | Sales                  |           3 | Life Sciences    |               1 |
|   97 |              153 |    34 | No          | Research & Development |           3 | Medical          |               1 |
|   98 |              154 |    36 | No          | Sales                  |           2 | Technical Degree |               1 |
|   99 |              155 |    36 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  100 |              158 |    43 | No          | Sales                  |           2 | Life Sciences    |               1 |
|  101 |              159 |    30 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  102 |              160 |    33 | No          | Sales                  |           2 | Marketing        |               1 |
|  103 |              162 |    51 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  104 |              164 |    26 | No          | Research & Development |           3 | Other            |               1 |
|  105 |              169 |    22 | No          | Research & Development |           1 | Technical Degree |               1 |
|  106 |              170 |    49 | No          | Research & Development |           4 | Medical          |               1 |
|  107 |              171 |    43 | No          | Research & Development |           3 | Medical          |               1 |
|  108 |              174 |    50 | No          | Sales                  |           3 | Marketing        |               1 |
|  109 |              176 |    41 | No          | Sales                  |           1 | Life Sciences    |               1 |
|  110 |              177 |    26 | No          | Human Resources        |           1 | Life Sciences    |               1 |
|  111 |              178 |    36 | No          | Research & Development |           2 | Medical          |               1 |
|  112 |              182 |    39 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  113 |              183 |    25 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  114 |              184 |    30 | No          | Human Resources        |           3 | Human Resources  |               1 |
|  115 |              192 |    45 | No          | Research & Development |           3 | Medical          |               1 |
|  116 |              193 |    38 | No          | Research & Development |           5 | Technical Degree |               1 |
|  117 |              194 |    30 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  118 |              195 |    32 | No          | Sales                  |           2 | Medical          |               1 |
|  119 |              197 |    30 | No          | Research & Development |           3 | Technical Degree |               1 |
|  120 |              198 |    30 | No          | Research & Development |           1 | Medical          |               1 |
|  121 |              199 |    41 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  122 |              200 |    41 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  123 |              201 |    19 | No          | Research & Development |           1 | Medical          |               1 |
|  124 |              202 |    40 | No          | Research & Development |           3 | Medical          |               1 |
|  125 |              204 |    35 | No          | Sales                  |           5 | Marketing        |               1 |
|  126 |              205 |    53 | No          | Sales                  |           2 | Marketing        |               1 |
|  127 |              206 |    45 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  128 |              207 |    32 | No          | Sales                  |           3 | Marketing        |               1 |
|  129 |              208 |    29 | No          | Research & Development |           1 | Technical Degree |               1 |
|  130 |              211 |    51 | No          | Research & Development |           4 | Medical          |               1 |
|  131 |              214 |    58 | No          | Research & Development |           3 | Medical          |               1 |
|  132 |              215 |    40 | No          | Sales                  |           4 | Marketing        |               1 |
|  133 |              216 |    34 | No          | Sales                  |           4 | Marketing        |               1 |
|  134 |              217 |    22 | No          | Research & Development |           1 | Medical          |               1 |
|  135 |              218 |    27 | No          | Research & Development |           3 | Medical          |               1 |
|  136 |              221 |    28 | No          | Research & Development |           3 | Medical          |               1 |
|  137 |              223 |    57 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  138 |              224 |    27 | No          | Research & Development |           3 | Medical          |               1 |
|  139 |              226 |    50 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  140 |              227 |    41 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  141 |              228 |    30 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  142 |              230 |    38 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  143 |              231 |    32 | No          | Research & Development |           5 | Life Sciences    |               1 |
|  144 |              233 |    27 | No          | Research & Development |           3 | Technical Degree |               1 |
|  145 |              238 |    36 | No          | Research & Development |           2 | Medical          |               1 |
|  146 |              239 |    30 | No          | Research & Development |           3 | Medical          |               1 |
|  147 |              240 |    45 | No          | Sales                  |           2 | Life Sciences    |               1 |
|  148 |              241 |    56 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  149 |              242 |    33 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  150 |              244 |    46 | No          | Sales                  |           2 | Marketing        |               1 |
|  151 |              245 |    38 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  152 |              246 |    31 | No          | Research & Development |           1 | Medical          |               1 |
|  153 |              247 |    34 | No          | Research & Development |           2 | Medical          |               1 |
|  154 |              249 |    50 | No          | Research & Development |           3 | Medical          |               1 |
|  155 |              250 |    53 | No          | Research & Development |           2 | Medical          |               1 |
|  156 |              252 |    33 | No          | Research & Development |           3 | Medical          |               1 |
|  157 |              253 |    40 | No          | Research & Development |           1 | Medical          |               1 |
|  158 |              254 |    55 | No          | Research & Development |           4 | Medical          |               1 |
|  159 |              256 |    34 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  160 |              258 |    51 | No          | Research & Development |           3 | Medical          |               1 |
|  161 |              259 |    52 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  162 |              260 |    27 | No          | Research & Development |           3 | Medical          |               1 |
|  163 |              262 |    43 | No          | Research & Development |           3 | Medical          |               1 |
|  164 |              264 |    45 | No          | Research & Development |           2 | Medical          |               1 |
|  165 |              267 |    37 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  166 |              269 |    35 | No          | Research & Development |           3 | Medical          |               1 |
|  167 |              270 |    42 | No          | Research & Development |           2 | Medical          |               1 |
|  168 |              271 |    38 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  169 |              273 |    38 | No          | Research & Development |           3 | Technical Degree |               1 |
|  170 |              274 |    27 | No          | Research & Development |           1 | Technical Degree |               1 |
|  171 |              275 |    49 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  172 |              277 |    34 | No          | Research & Development |           4 | Medical          |               1 |
|  173 |              281 |    40 | No          | Research & Development |           2 | Medical          |               1 |
|  174 |              284 |    22 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  175 |              286 |    36 | No          | Research & Development |           1 | Medical          |               1 |
|  176 |              287 |    40 | No          | Research & Development |           5 | Life Sciences    |               1 |
|  177 |              288 |    46 | No          | Research & Development |           4 | Medical          |               1 |
|  178 |              292 |    30 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  179 |              293 |    27 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  180 |              296 |    51 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  181 |              298 |    41 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  182 |              302 |    45 | No          | Sales                  |           3 | Medical          |               1 |
|  183 |              303 |    54 | No          | Sales                  |           3 | Marketing        |               1 |
|  184 |              304 |    36 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  185 |              305 |    33 | No          | Research & Development |           4 | Medical          |               1 |
|  186 |              306 |    37 | No          | Research & Development |           3 | Other            |               1 |
|  187 |              307 |    38 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  188 |              308 |    31 | No          | Research & Development |           4 | Medical          |               1 |
|  189 |              309 |    59 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  190 |              311 |    37 | No          | Sales                  |           4 | Marketing        |               1 |
|  191 |              312 |    29 | No          | Sales                  |           1 | Medical          |               1 |
|  192 |              314 |    35 | No          | Sales                  |           3 | Marketing        |               1 |
|  193 |              316 |    52 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  194 |              319 |    42 | No          | Research & Development |           2 | Technical Degree |               1 |
|  195 |              321 |    59 | No          | Human Resources        |           2 | Medical          |               1 |
|  196 |              323 |    50 | No          | Sales                  |           4 | Medical          |               1 |
|  197 |              327 |    43 | No          | Sales                  |           3 | Marketing        |               1 |
|  198 |              329 |    52 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  199 |              330 |    32 | No          | Sales                  |           2 | Life Sciences    |               1 |
|  200 |              332 |    39 | No          | Research & Development |           4 | Medical          |               1 |
|  201 |              333 |    32 | No          | Sales                  |           4 | Marketing        |               1 |
|  202 |              334 |    41 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  203 |              335 |    40 | No          | Research & Development |           2 | Technical Degree |               1 |
|  204 |              336 |    45 | No          | Research & Development |           3 | Other            |               1 |
|  205 |              337 |    31 | No          | Research & Development |           4 | Medical          |               1 |
|  206 |              338 |    33 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  207 |              339 |    34 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  208 |              340 |    37 | No          | Research & Development |           2 | Medical          |               1 |
|  209 |              341 |    45 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  210 |              343 |    39 | No          | Research & Development |           4 | Technical Degree |               1 |
|  211 |              346 |    29 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  212 |              347 |    42 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  213 |              349 |    29 | No          | Sales                  |           2 | Marketing        |               1 |
|  214 |              350 |    25 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  215 |              351 |    42 | No          | Research & Development |           3 | Medical          |               1 |
|  216 |              352 |    40 | No          | Research & Development |           2 | Medical          |               1 |
|  217 |              353 |    51 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  218 |              359 |    32 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  219 |              361 |    38 | No          | Sales                  |           2 | Life Sciences    |               1 |
|  220 |              362 |    32 | No          | Research & Development |           1 | Technical Degree |               1 |
|  221 |              363 |    46 | No          | Sales                  |           3 | Technical Degree |               1 |
|  222 |              366 |    29 | No          | Sales                  |           3 | Medical          |               1 |
|  223 |              367 |    31 | No          | Research & Development |           3 | Medical          |               1 |
|  224 |              369 |    25 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  225 |              372 |    45 | No          | Research & Development |           2 | Medical          |               1 |
|  226 |              373 |    36 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  227 |              374 |    55 | No          | Research & Development |           3 | Medical          |               1 |
|  228 |              377 |    28 | No          | Research & Development |           3 | Medical          |               1 |
|  229 |              378 |    37 | No          | Sales                  |           4 | Medical          |               1 |
|  230 |              379 |    21 | No          | Research & Development |           2 | Medical          |               1 |
|  231 |              380 |    37 | No          | Research & Development |           4 | Medical          |               1 |
|  232 |              381 |    35 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  233 |              382 |    38 | No          | Sales                  |           2 | Medical          |               1 |
|  234 |              384 |    26 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  235 |              385 |    50 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  236 |              386 |    53 | No          | Research & Development |           4 | Medical          |               1 |
|  237 |              387 |    42 | No          | Sales                  |           1 | Life Sciences    |               1 |
|  238 |              388 |    29 | No          | Sales                  |           2 | Life Sciences    |               1 |
|  239 |              389 |    55 | No          | Research & Development |           2 | Technical Degree |               1 |
|  240 |              390 |    26 | No          | Research & Development |           2 | Medical          |               1 |
|  241 |              391 |    37 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  242 |              393 |    38 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  243 |              395 |    28 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  244 |              396 |    49 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  245 |              397 |    36 | No          | Research & Development |           3 | Technical Degree |               1 |
|  246 |              399 |    31 | No          | Sales                  |           3 | Marketing        |               1 |
|  247 |              403 |    37 | No          | Research & Development |           3 | Medical          |               1 |
|  248 |              404 |    42 | No          | Sales                  |           3 | Marketing        |               1 |
|  249 |              406 |    35 | No          | Sales                  |           3 | Marketing        |               1 |
|  250 |              407 |    36 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  251 |              408 |    51 | No          | Research & Development |           3 | Medical          |               1 |
|  252 |              410 |    41 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  253 |              411 |    18 | No          | Sales                  |           3 | Medical          |               1 |
|  254 |              412 |    28 | No          | Research & Development |           2 | Medical          |               1 |
|  255 |              416 |    31 | No          | Sales                  |           3 | Technical Degree |               1 |
|  256 |              417 |    39 | No          | Research & Development |           3 | Medical          |               1 |
|  257 |              419 |    36 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  258 |              420 |    32 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  259 |              421 |    38 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  260 |              422 |    58 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  261 |              423 |    31 | No          | Research & Development |           4 | Technical Degree |               1 |
|  262 |              424 |    31 | No          | Human Resources        |           3 | Human Resources  |               1 |
|  263 |              425 |    45 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  264 |              426 |    31 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  265 |              428 |    33 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  266 |              429 |    39 | No          | Research & Development |           1 | Medical          |               1 |
|  267 |              430 |    43 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  268 |              431 |    49 | No          | Research & Development |           2 | Technical Degree |               1 |
|  269 |              434 |    27 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  270 |              436 |    32 | No          | Sales                  |           2 | Technical Degree |               1 |
|  271 |              437 |    27 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  272 |              438 |    31 | No          | Sales                  |           3 | Marketing        |               1 |
|  273 |              439 |    32 | No          | Research & Development |           4 | Medical          |               1 |
|  274 |              441 |    30 | No          | Research & Development |           2 | Medical          |               1 |
|  275 |              442 |    31 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  276 |              444 |    39 | No          | Research & Development |           2 | Medical          |               1 |
|  277 |              446 |    33 | No          | Sales                  |           3 | Marketing        |               1 |
|  278 |              447 |    47 | No          | Research & Development |           5 | Life Sciences    |               1 |
|  279 |              448 |    43 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  280 |              449 |    27 | No          | Sales                  |           1 | Marketing        |               1 |
|  281 |              450 |    54 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  282 |              451 |    43 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  283 |              452 |    45 | No          | Research & Development |           4 | Other            |               1 |
|  284 |              453 |    40 | No          | Sales                  |           2 | Medical          |               1 |
|  285 |              455 |    29 | No          | Research & Development |           5 | Other            |               1 |
|  286 |              456 |    30 | No          | Sales                  |           3 | Marketing        |               1 |
|  287 |              458 |    27 | No          | Sales                  |           4 | Marketing        |               1 |
|  288 |              460 |    37 | No          | Research & Development |           2 | Medical          |               1 |
|  289 |              461 |    38 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  290 |              462 |    31 | No          | Research & Development |           4 | Medical          |               1 |
|  291 |              463 |    29 | No          | Sales                  |           1 | Marketing        |               1 |
|  292 |              464 |    35 | No          | Research & Development |           4 | Technical Degree |               1 |
|  293 |              465 |    23 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  294 |              466 |    41 | No          | Research & Development |           3 | Medical          |               1 |
|  295 |              467 |    47 | No          | Sales                  |           1 | Medical          |               1 |
|  296 |              468 |    42 | No          | Research & Development |           5 | Life Sciences    |               1 |
|  297 |              469 |    29 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  298 |              470 |    42 | No          | Human Resources        |           1 | Technical Degree |               1 |
|  299 |              471 |    32 | No          | Research & Development |           3 | Medical          |               1 |
|  300 |              473 |    48 | No          | Sales                  |           1 | Medical          |               1 |
|  301 |              474 |    37 | No          | Research & Development |           3 | Medical          |               1 |
|  302 |              475 |    30 | No          | Sales                  |           2 | Technical Degree |               1 |
|  303 |              476 |    26 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  304 |              477 |    42 | No          | Research & Development |           4 | Other            |               1 |
|  305 |              479 |    36 | No          | Sales                  |           5 | Medical          |               1 |
|  306 |              481 |    36 | No          | Sales                  |           4 | Medical          |               1 |
|  307 |              482 |    57 | No          | Research & Development |           4 | Medical          |               1 |
|  308 |              483 |    40 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  309 |              484 |    21 | No          | Sales                  |           2 | Medical          |               1 |
|  310 |              486 |    37 | No          | Research & Development |           3 | Medical          |               1 |
|  311 |              487 |    46 | No          | Research & Development |           4 | Medical          |               1 |
|  312 |              491 |    50 | No          | Research & Development |           3 | Technical Degree |               1 |
|  313 |              493 |    31 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  314 |              495 |    29 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  315 |              496 |    35 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  316 |              497 |    27 | No          | Research & Development |           2 | Medical          |               1 |
|  317 |              498 |    28 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  318 |              499 |    49 | No          | Research & Development |           3 | Other            |               1 |
|  319 |              500 |    51 | No          | Sales                  |           2 | Life Sciences    |               1 |
|  320 |              501 |    36 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  321 |              505 |    55 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  322 |              507 |    24 | No          | Sales                  |           4 | Marketing        |               1 |
|  323 |              508 |    30 | No          | Sales                  |           1 | Technical Degree |               1 |
|  324 |              511 |    22 | No          | Research & Development |           3 | Medical          |               1 |
|  325 |              513 |    36 | No          | Sales                  |           2 | Medical          |               1 |
|  326 |              515 |    37 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  327 |              516 |    40 | No          | Sales                  |           2 | Marketing        |               1 |
|  328 |              517 |    42 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  329 |              518 |    37 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  330 |              520 |    43 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  331 |              521 |    40 | No          | Research & Development |           3 | Medical          |               1 |
|  332 |              522 |    54 | No          | Research & Development |           2 | Medical          |               1 |
|  333 |              523 |    34 | No          | Sales                  |           4 | Marketing        |               1 |
|  334 |              524 |    31 | No          | Research & Development |           2 | Medical          |               1 |
|  335 |              525 |    43 | No          | Research & Development |           3 | Medical          |               1 |
|  336 |              526 |    43 | No          | Research & Development |           4 | Other            |               1 |
|  337 |              527 |    25 | No          | Sales                  |           2 | Life Sciences    |               1 |
|  338 |              529 |    37 | No          | Research & Development |           5 | Medical          |               1 |
|  339 |              530 |    31 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  340 |              531 |    39 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  341 |              532 |    56 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  342 |              533 |    30 | No          | Sales                  |           3 | Technical Degree |               1 |
|  343 |              534 |    41 | No          | Sales                  |           3 | Marketing        |               1 |
|  344 |              536 |    28 | No          | Research & Development |           2 | Medical          |               1 |
|  345 |              543 |    52 | No          | Research & Development |           3 | Medical          |               1 |
|  346 |              544 |    45 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  347 |              546 |    52 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  348 |              547 |    42 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  349 |              548 |    30 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  350 |              549 |    60 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  351 |              550 |    46 | No          | Research & Development |           3 | Medical          |               1 |
|  352 |              551 |    42 | No          | Research & Development |           4 | Technical Degree |               1 |
|  353 |              556 |    38 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  354 |              558 |    40 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  355 |              560 |    26 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  356 |              562 |    30 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  357 |              564 |    29 | No          | Research & Development |           4 | Medical          |               1 |
|  358 |              567 |    30 | No          | Sales                  |           4 | Other            |               1 |
|  359 |              568 |    57 | No          | Sales                  |           3 | Marketing        |               1 |
|  360 |              569 |    50 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  361 |              571 |    30 | No          | Research & Development |           3 | Medical          |               1 |
|  362 |              573 |    60 | No          | Sales                  |           3 | Marketing        |               1 |
|  363 |              574 |    47 | No          | Research & Development |           2 | Medical          |               1 |
|  364 |              575 |    46 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  365 |              577 |    35 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  366 |              578 |    54 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  367 |              579 |    34 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  368 |              580 |    46 | No          | Sales                  |           3 | Marketing        |               1 |
|  369 |              581 |    31 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  370 |              585 |    30 | No          | Sales                  |           1 | Marketing        |               1 |
|  371 |              586 |    35 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  372 |              591 |    42 | No          | Research & Development |           2 | Other            |               1 |
|  373 |              592 |    36 | No          | Sales                  |           4 | Medical          |               1 |
|  374 |              595 |    48 | No          | Sales                  |           5 | Marketing        |               1 |
|  375 |              597 |    55 | No          | Sales                  |           5 | Life Sciences    |               1 |
|  376 |              599 |    41 | No          | Sales                  |           2 | Life Sciences    |               1 |
|  377 |              600 |    35 | No          | Sales                  |           3 | Marketing        |               1 |
|  378 |              601 |    40 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  379 |              602 |    39 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  380 |              604 |    31 | No          | Sales                  |           1 | Life Sciences    |               1 |
|  381 |              605 |    42 | No          | Research & Development |           3 | Medical          |               1 |
|  382 |              606 |    45 | No          | Sales                  |           3 | Other            |               1 |
|  383 |              611 |    29 | No          | Research & Development |           3 | Technical Degree |               1 |
|  384 |              612 |    33 | No          | Research & Development |           5 | Medical          |               1 |
|  385 |              613 |    31 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  386 |              615 |    40 | No          | Sales                  |           3 | Other            |               1 |
|  387 |              616 |    41 | No          | Research & Development |           4 | Other            |               1 |
|  388 |              618 |    26 | No          | Sales                  |           2 | Medical          |               1 |
|  389 |              620 |    35 | No          | Sales                  |           3 | Medical          |               1 |
|  390 |              621 |    34 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  391 |              623 |    37 | No          | Research & Development |           3 | Technical Degree |               1 |
|  392 |              624 |    46 | No          | Research & Development |           1 | Medical          |               1 |
|  393 |              625 |    41 | No          | Sales                  |           5 | Life Sciences    |               1 |
|  394 |              626 |    37 | No          | Sales                  |           4 | Medical          |               1 |
|  395 |              630 |    52 | No          | Research & Development |           2 | Technical Degree |               1 |
|  396 |              632 |    24 | No          | Sales                  |           3 | Medical          |               1 |
|  397 |              634 |    38 | No          | Research & Development |           3 | Medical          |               1 |
|  398 |              635 |    37 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  399 |              638 |    49 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  400 |              639 |    24 | No          | Research & Development |           3 | Medical          |               1 |
|  401 |              641 |    26 | No          | Sales                  |           2 | Marketing        |               1 |
|  402 |              643 |    24 | No          | Research & Development |           2 | Other            |               1 |
|  403 |              644 |    50 | No          | Human Resources        |           3 | Medical          |               1 |
|  404 |              645 |    25 | No          | Sales                  |           1 | Medical          |               1 |
|  405 |              649 |    34 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  406 |              652 |    35 | No          | Research & Development |           2 | Other            |               1 |
|  407 |              653 |    31 | No          | Sales                  |           4 | Medical          |               1 |
|  408 |              655 |    27 | No          | Research & Development |           4 | Medical          |               1 |
|  409 |              656 |    37 | No          | Sales                  |           3 | Marketing        |               1 |
|  410 |              657 |    20 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  411 |              659 |    42 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  412 |              661 |    43 | No          | Research & Development |           4 | Other            |               1 |
|  413 |              662 |    38 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  414 |              663 |    43 | No          | Research & Development |           5 | Medical          |               1 |
|  415 |              664 |    48 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  416 |              665 |    44 | No          | Human Resources        |           4 | Life Sciences    |               1 |
|  417 |              666 |    34 | No          | Sales                  |           3 | Technical Degree |               1 |
|  418 |              669 |    21 | No          | Sales                  |           1 | Technical Degree |               1 |
|  419 |              671 |    44 | No          | Research & Development |           4 | Other            |               1 |
|  420 |              675 |    22 | No          | Research & Development |           1 | Medical          |               1 |
|  421 |              677 |    33 | No          | Sales                  |           4 | Marketing        |               1 |
|  422 |              679 |    32 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  423 |              680 |    30 | No          | Research & Development |           3 | Medical          |               1 |
|  424 |              682 |    53 | No          | Sales                  |           1 | Medical          |               1 |
|  425 |              683 |    34 | No          | Research & Development |           5 | Life Sciences    |               1 |
|  426 |              686 |    26 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  427 |              689 |    37 | No          | Research & Development |           3 | Other            |               1 |
|  428 |              690 |    29 | No          | Sales                  |           2 | Medical          |               1 |
|  429 |              691 |    35 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  430 |              692 |    33 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  431 |              698 |    54 | No          | Human Resources        |           4 | Medical          |               1 |
|  432 |              699 |    36 | No          | Research & Development |           2 | Medical          |               1 |
|  433 |              700 |    27 | No          | Research & Development |           4 | Medical          |               1 |
|  434 |              704 |    35 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  435 |              705 |    23 | No          | Research & Development |           3 | Medical          |               1 |
|  436 |              707 |    25 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  437 |              709 |    38 | No          | Sales                  |           4 | Marketing        |               1 |
|  438 |              710 |    29 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  439 |              712 |    48 | No          | Sales                  |           1 | Marketing        |               1 |
|  440 |              714 |    27 | No          | Sales                  |           1 | Medical          |               1 |
|  441 |              715 |    37 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  442 |              716 |    50 | No          | Research & Development |           1 | Medical          |               1 |
|  443 |              717 |    34 | No          | Research & Development |           3 | Medical          |               1 |
|  444 |              721 |    39 | No          | Research & Development |           4 | Technical Degree |               1 |
|  445 |              722 |    32 | No          | Sales                  |           3 | Marketing        |               1 |
|  446 |              724 |    38 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  447 |              725 |    27 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  448 |              727 |    32 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  449 |              728 |    47 | No          | Sales                  |           4 | Marketing        |               1 |
|  450 |              729 |    40 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  451 |              730 |    53 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  452 |              731 |    41 | No          | Human Resources        |           4 | Human Resources  |               1 |
|  453 |              732 |    60 | No          | Sales                  |           4 | Marketing        |               1 |
|  454 |              733 |    27 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  455 |              734 |    41 | No          | Human Resources        |           3 | Human Resources  |               1 |
|  456 |              738 |    50 | No          | Sales                  |           4 | Marketing        |               1 |
|  457 |              742 |    36 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  458 |              743 |    38 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  459 |              744 |    44 | No          | Research & Development |           3 | Medical          |               1 |
|  460 |              746 |    47 | No          | Sales                  |           3 | Medical          |               1 |
|  461 |              747 |    30 | No          | Sales                  |           5 | Marketing        |               1 |
|  462 |              749 |    29 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  463 |              754 |    43 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  464 |              757 |    34 | No          | Research & Development |           2 | Medical          |               1 |
|  465 |              758 |    23 | No          | Research & Development |           1 | Medical          |               1 |
|  466 |              760 |    39 | No          | Human Resources        |           3 | Human Resources  |               1 |
|  467 |              762 |    56 | No          | Research & Development |           3 | Medical          |               1 |
|  468 |              763 |    40 | No          | Research & Development |           1 | Medical          |               1 |
|  469 |              764 |    27 | No          | Research & Development |           3 | Medical          |               1 |
|  470 |              766 |    29 | No          | Sales                  |           3 | Marketing        |               1 |
|  471 |              769 |    53 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  472 |              771 |    35 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  473 |              772 |    32 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  474 |              773 |    38 | No          | Research & Development |           5 | Medical          |               1 |
|  475 |              775 |    34 | No          | Research & Development |           5 | Life Sciences    |               1 |
|  476 |              776 |    52 | No          | Sales                  |           4 | Marketing        |               1 |
|  477 |              781 |    25 | No          | Sales                  |           1 | Medical          |               1 |
|  478 |              783 |    45 | No          | Sales                  |           2 | Technical Degree |               1 |
|  479 |              784 |    23 | No          | Research & Development |           1 | Medical          |               1 |
|  480 |              786 |    34 | No          | Sales                  |           3 | Other            |               1 |
|  481 |              789 |    36 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  482 |              791 |    52 | No          | Research & Development |           4 | Medical          |               1 |
|  483 |              792 |    26 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  484 |              793 |    29 | No          | Research & Development |           3 | Medical          |               1 |
|  485 |              797 |    34 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  486 |              799 |    54 | No          | Research & Development |           4 | Medical          |               1 |
|  487 |              800 |    27 | No          | Sales                  |           1 | Marketing        |               1 |
|  488 |              802 |    37 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  489 |              803 |    38 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  490 |              804 |    34 | No          | Research & Development |           4 | Medical          |               1 |
|  491 |              805 |    35 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  492 |              806 |    30 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  493 |              807 |    40 | No          | Research & Development |           2 | Medical          |               1 |
|  494 |              808 |    34 | No          | Sales                  |           2 | Life Sciences    |               1 |
|  495 |              809 |    42 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  496 |              812 |    24 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  497 |              813 |    52 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  498 |              815 |    50 | No          | Research & Development |           3 | Medical          |               1 |
|  499 |              817 |    33 | No          | Research & Development |           3 | Medical          |               1 |
|  500 |              820 |    47 | No          | Research & Development |           2 | Other            |               1 |
|  501 |              823 |    36 | No          | Research & Development |           3 | Other            |               1 |
|  502 |              824 |    29 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  503 |              826 |    35 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  504 |              827 |    42 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  505 |              829 |    36 | No          | Human Resources        |           3 | Human Resources  |               1 |
|  506 |              830 |    32 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  507 |              832 |    40 | No          | Research & Development |           4 | Medical          |               1 |
|  508 |              833 |    30 | No          | Research & Development |           3 | Medical          |               1 |
|  509 |              834 |    45 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  510 |              836 |    42 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  511 |              837 |    38 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  512 |              838 |    34 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  513 |              843 |    43 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  514 |              844 |    27 | No          | Research & Development |           1 | Technical Degree |               1 |
|  515 |              845 |    35 | No          | Research & Development |           3 | Other            |               1 |
|  516 |              846 |    28 | No          | Sales                  |           4 | Marketing        |               1 |
|  517 |              847 |    34 | No          | Human Resources        |           2 | Human Resources  |               1 |
|  518 |              850 |    27 | No          | Research & Development |           3 | Medical          |               1 |
|  519 |              851 |    51 | No          | Sales                  |           4 | Marketing        |               1 |
|  520 |              852 |    44 | No          | Research & Development |           3 | Medical          |               1 |
|  521 |              854 |    25 | No          | Research & Development |           1 | Medical          |               1 |
|  522 |              855 |    33 | No          | Sales                  |           3 | Medical          |               1 |
|  523 |              856 |    35 | No          | Research & Development |           1 | Medical          |               1 |
|  524 |              857 |    36 | No          | Sales                  |           2 | Life Sciences    |               1 |
|  525 |              859 |    32 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  526 |              861 |    30 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  527 |              862 |    53 | No          | Sales                  |           2 | Marketing        |               1 |
|  528 |              864 |    45 | No          | Sales                  |           3 | Marketing        |               1 |
|  529 |              865 |    32 | No          | Research & Development |           2 | Medical          |               1 |
|  530 |              867 |    52 | No          | Research & Development |           4 | Medical          |               1 |
|  531 |              868 |    37 | No          | Sales                  |           4 | Marketing        |               1 |
|  532 |              869 |    28 | No          | Human Resources        |           2 | Medical          |               1 |
|  533 |              872 |    22 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  534 |              874 |    44 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  535 |              875 |    42 | No          | Research & Development |           1 | Medical          |               1 |
|  536 |              878 |    36 | No          | Human Resources        |           3 | Life Sciences    |               1 |
|  537 |              879 |    25 | No          | Sales                  |           1 | Other            |               1 |
|  538 |              880 |    35 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  539 |              882 |    32 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  540 |              885 |    25 | No          | Sales                  |           1 | Marketing        |               1 |
|  541 |              887 |    49 | No          | Research & Development |           3 | Technical Degree |               1 |
|  542 |              888 |    24 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  543 |              889 |    32 | No          | Sales                  |           2 | Life Sciences    |               1 |
|  544 |              893 |    38 | No          | Sales                  |           3 | Marketing        |               1 |
|  545 |              894 |    42 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  546 |              895 |    31 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  547 |              897 |    53 | No          | Sales                  |           3 | Marketing        |               1 |
|  548 |              899 |    35 | No          | Research & Development |           3 | Technical Degree |               1 |
|  549 |              900 |    37 | No          | Sales                  |           2 | Medical          |               1 |
|  550 |              901 |    53 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  551 |              902 |    43 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  552 |              903 |    47 | No          | Sales                  |           2 | Marketing        |               1 |
|  553 |              904 |    37 | No          | Sales                  |           2 | Medical          |               1 |
|  554 |              905 |    50 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  555 |              909 |    39 | No          | Human Resources        |           3 | Life Sciences    |               1 |
|  556 |              910 |    33 | No          | Human Resources        |           2 | Human Resources  |               1 |
|  557 |              912 |    29 | No          | Research & Development |           1 | Medical          |               1 |
|  558 |              913 |    44 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  559 |              916 |    28 | No          | Sales                  |           4 | Medical          |               1 |
|  560 |              920 |    43 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  561 |              924 |    36 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  562 |              925 |    47 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  563 |              930 |    28 | No          | Research & Development |           3 | Medical          |               1 |
|  564 |              933 |    27 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  565 |              934 |    34 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  566 |              936 |    42 | No          | Sales                  |           2 | Medical          |               1 |
|  567 |              939 |    33 | No          | Research & Development |           4 | Other            |               1 |
|  568 |              940 |    58 | No          | Research & Development |           3 | Technical Degree |               1 |
|  569 |              941 |    31 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  570 |              942 |    35 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  571 |              944 |    49 | No          | Research & Development |           2 | Other            |               1 |
|  572 |              945 |    48 | No          | Research & Development |           4 | Medical          |               1 |
|  573 |              947 |    31 | No          | Sales                  |           2 | Marketing        |               1 |
|  574 |              949 |    36 | No          | Research & Development |           4 | Other            |               1 |
|  575 |              950 |    38 | No          | Research & Development |           3 | Technical Degree |               1 |
|  576 |              951 |    32 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  577 |              954 |    40 | No          | Sales                  |           4 | Marketing        |               1 |
|  578 |              956 |    26 | No          | Sales                  |           3 | Medical          |               1 |
|  579 |              957 |    41 | No          | Research & Development |           3 | Medical          |               1 |
|  580 |              958 |    36 | No          | Research & Development |           4 | Medical          |               1 |
|  581 |              961 |    31 | No          | Research & Development |           3 | Medical          |               1 |
|  582 |              964 |    40 | No          | Research & Development |           4 | Medical          |               1 |
|  583 |              966 |    32 | No          | Research & Development |           4 | Medical          |               1 |
|  584 |              969 |    33 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  585 |              972 |    45 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  586 |              974 |    29 | No          | Sales                  |           3 | Technical Degree |               1 |
|  587 |              975 |    35 | No          | Sales                  |           3 | Medical          |               1 |
|  588 |              976 |    52 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  589 |              981 |    53 | No          | Sales                  |           2 | Medical          |               1 |
|  590 |              982 |    30 | No          | Sales                  |           2 | Other            |               1 |
|  591 |              983 |    38 | No          | Sales                  |           3 | Technical Degree |               1 |
|  592 |              984 |    35 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  593 |              985 |    39 | No          | Sales                  |           5 | Life Sciences    |               1 |
|  594 |              987 |    47 | No          | Research & Development |           4 | Medical          |               1 |
|  595 |              990 |    36 | No          | Sales                  |           4 | Technical Degree |               1 |
|  596 |              992 |    33 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  597 |              995 |    33 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  598 |              996 |    45 | No          | Research & Development |           4 | Medical          |               1 |
|  599 |              997 |    50 | No          | Research & Development |           2 | Medical          |               1 |
|  600 |              998 |    33 | No          | Research & Development |           4 | Other            |               1 |
|  601 |              999 |    41 | No          | Research & Development |           3 | Medical          |               1 |
|  602 |             1001 |    27 | No          | Research & Development |           4 | Technical Degree |               1 |
|  603 |             1002 |    45 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  604 |             1003 |    47 | No          | Sales                  |           2 | Life Sciences    |               1 |
|  605 |             1005 |    50 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  606 |             1006 |    38 | No          | Research & Development |           1 | Medical          |               1 |
|  607 |             1007 |    46 | No          | Research & Development |           2 | Medical          |               1 |
|  608 |             1009 |    24 | No          | Research & Development |           1 | Medical          |               1 |
|  609 |             1011 |    31 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  610 |             1012 |    18 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  611 |             1013 |    54 | No          | Research & Development |           3 | Technical Degree |               1 |
|  612 |             1014 |    35 | No          | Research & Development |           4 | Medical          |               1 |
|  613 |             1015 |    30 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  614 |             1018 |    26 | No          | Research & Development |           2 | Medical          |               1 |
|  615 |             1019 |    22 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  616 |             1022 |    48 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  617 |             1024 |    48 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  618 |             1025 |    41 | No          | Research & Development |           2 | Medical          |               1 |
|  619 |             1026 |    39 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  620 |             1027 |    27 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  621 |             1028 |    35 | No          | Research & Development |           3 | Other            |               1 |
|  622 |             1029 |    42 | No          | Sales                  |           2 | Marketing        |               1 |
|  623 |             1030 |    50 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  624 |             1032 |    59 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  625 |             1034 |    55 | No          | Research & Development |           4 | Medical          |               1 |
|  626 |             1035 |    41 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  627 |             1036 |    38 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  628 |             1039 |    44 | No          | Sales                  |           3 | Medical          |               1 |
|  629 |             1040 |    50 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  630 |             1043 |    39 | No          | Research & Development |           3 | Medical          |               1 |
|  631 |             1044 |    33 | No          | Sales                  |           1 | Life Sciences    |               1 |
|  632 |             1045 |    45 | No          | Sales                  |           2 | Life Sciences    |               1 |
|  633 |             1046 |    32 | No          | Research & Development |           4 | Medical          |               1 |
|  634 |             1047 |    34 | No          | Sales                  |           4 | Marketing        |               1 |
|  635 |             1048 |    59 | No          | Sales                  |           2 | Technical Degree |               1 |
|  636 |             1049 |    45 | No          | Human Resources        |           4 | Medical          |               1 |
|  637 |             1050 |    53 | No          | Sales                  |           3 | Marketing        |               1 |
|  638 |             1055 |    34 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  639 |             1056 |    28 | No          | Sales                  |           1 | Medical          |               1 |
|  640 |             1060 |    38 | No          | Research & Development |           4 | Other            |               1 |
|  641 |             1061 |    50 | No          | Research & Development |           4 | Medical          |               1 |
|  642 |             1062 |    37 | No          | Research & Development |           3 | Other            |               1 |
|  643 |             1066 |    40 | No          | Sales                  |           3 | Marketing        |               1 |
|  644 |             1068 |    26 | No          | Research & Development |           1 | Medical          |               1 |
|  645 |             1069 |    46 | No          | Research & Development |           4 | Medical          |               1 |
|  646 |             1070 |    54 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  647 |             1071 |    56 | No          | Research & Development |           3 | Medical          |               1 |
|  648 |             1073 |    36 | No          | Research & Development |           5 | Medical          |               1 |
|  649 |             1074 |    55 | No          | Research & Development |           1 | Medical          |               1 |
|  650 |             1076 |    43 | No          | Sales                  |           3 | Medical          |               1 |
|  651 |             1080 |    46 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  652 |             1083 |    26 | No          | Research & Development |           2 | Medical          |               1 |
|  653 |             1084 |    30 | No          | Research & Development |           3 | Other            |               1 |
|  654 |             1085 |    41 | No          | Research & Development |           2 | Technical Degree |               1 |
|  655 |             1088 |    38 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  656 |             1092 |    40 | No          | Research & Development |           4 | Technical Degree |               1 |
|  657 |             1094 |    27 | No          | Research & Development |           5 | Life Sciences    |               1 |
|  658 |             1096 |    55 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  659 |             1097 |    28 | No          | Research & Development |           3 | Other            |               1 |
|  660 |             1099 |    33 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  661 |             1102 |    28 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  662 |             1103 |    34 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  663 |             1105 |    37 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  664 |             1109 |    42 | No          | Research & Development |           2 | Medical          |               1 |
|  665 |             1114 |    33 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  666 |             1115 |    34 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  667 |             1116 |    48 | No          | Research & Development |           4 | Medical          |               1 |
|  668 |             1117 |    45 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  669 |             1118 |    52 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  670 |             1119 |    38 | No          | Sales                  |           4 | Marketing        |               1 |
|  671 |             1120 |    29 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  672 |             1121 |    28 | No          | Research & Development |           3 | Medical          |               1 |
|  673 |             1124 |    46 | No          | Sales                  |           1 | Marketing        |               1 |
|  674 |             1125 |    38 | No          | Sales                  |           2 | Marketing        |               1 |
|  675 |             1126 |    43 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  676 |             1128 |    40 | No          | Research & Development |           3 | Medical          |               1 |
|  677 |             1131 |    21 | No          | Research & Development |           1 | Technical Degree |               1 |
|  678 |             1132 |    39 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  679 |             1133 |    36 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  680 |             1135 |    31 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  681 |             1136 |    28 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  682 |             1137 |    35 | No          | Sales                  |           2 | Marketing        |               1 |
|  683 |             1138 |    49 | No          | Sales                  |           4 | Technical Degree |               1 |
|  684 |             1140 |    34 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  685 |             1143 |    29 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  686 |             1148 |    42 | No          | Research & Development |           3 | Medical          |               1 |
|  687 |             1150 |    29 | No          | Research & Development |           1 | Medical          |               1 |
|  688 |             1152 |    38 | No          | Human Resources        |           3 | Human Resources  |               1 |
|  689 |             1154 |    28 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  690 |             1158 |    41 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  691 |             1161 |    37 | No          | Research & Development |           2 | Medical          |               1 |
|  692 |             1162 |    27 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  693 |             1163 |    34 | No          | Sales                  |           1 | Life Sciences    |               1 |
|  694 |             1164 |    35 | No          | Human Resources        |           4 | Technical Degree |               1 |
|  695 |             1166 |    40 | No          | Research & Development |           4 | Medical          |               1 |
|  696 |             1171 |    42 | No          | Sales                  |           4 | Marketing        |               1 |
|  697 |             1172 |    35 | No          | Research & Development |           4 | Medical          |               1 |
|  698 |             1173 |    24 | No          | Research & Development |           3 | Medical          |               1 |
|  699 |             1177 |    26 | No          | Research & Development |           4 | Medical          |               1 |
|  700 |             1179 |    30 | No          | Sales                  |           3 | Marketing        |               1 |
|  701 |             1180 |    40 | No          | Research & Development |           2 | Medical          |               1 |
|  702 |             1182 |    35 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  703 |             1184 |    34 | No          | Research & Development |           3 | Medical          |               1 |
|  704 |             1185 |    35 | No          | Research & Development |           4 | Other            |               1 |
|  705 |             1190 |    32 | No          | Sales                  |           1 | Life Sciences    |               1 |
|  706 |             1191 |    56 | No          | Research & Development |           4 | Technical Degree |               1 |
|  707 |             1192 |    29 | No          | Research & Development |           1 | Medical          |               1 |
|  708 |             1193 |    19 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  709 |             1195 |    45 | No          | Research & Development |           3 | Medical          |               1 |
|  710 |             1196 |    37 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  711 |             1198 |    20 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  712 |             1201 |    53 | No          | Research & Development |           2 | Medical          |               1 |
|  713 |             1202 |    29 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  714 |             1204 |    46 | No          | Sales                  |           3 | Marketing        |               1 |
|  715 |             1206 |    44 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  716 |             1207 |    33 | No          | Human Resources        |           3 | Human Resources  |               1 |
|  717 |             1211 |    30 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  718 |             1212 |    40 | No          | Sales                  |           4 | Medical          |               1 |
|  719 |             1215 |    50 | No          | Research & Development |           3 | Medical          |               1 |
|  720 |             1216 |    28 | No          | Research & Development |           4 | Medical          |               1 |
|  721 |             1217 |    46 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  722 |             1218 |    35 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  723 |             1220 |    33 | No          | Sales                  |           3 | Medical          |               1 |
|  724 |             1221 |    36 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  725 |             1224 |    30 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  726 |             1225 |    44 | No          | Research & Development |           4 | Other            |               1 |
|  727 |             1226 |    20 | No          | Sales                  |           3 | Marketing        |               1 |
|  728 |             1228 |    46 | No          | Research & Development |           4 | Technical Degree |               1 |
|  729 |             1231 |    42 | No          | Human Resources        |           5 | Medical          |               1 |
|  730 |             1233 |    60 | No          | Sales                  |           4 | Marketing        |               1 |
|  731 |             1234 |    32 | No          | Research & Development |           3 | Other            |               1 |
|  732 |             1235 |    32 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  733 |             1237 |    36 | No          | Research & Development |           3 | Technical Degree |               1 |
|  734 |             1238 |    33 | No          | Research & Development |           3 | Medical          |               1 |
|  735 |             1239 |    40 | No          | Sales                  |           3 | Technical Degree |               1 |
|  736 |             1240 |    25 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  737 |             1241 |    30 | No          | Research & Development |           3 | Medical          |               1 |
|  738 |             1242 |    42 | No          | Research & Development |           5 | Medical          |               1 |
|  739 |             1243 |    35 | No          | Sales                  |           2 | Marketing        |               1 |
|  740 |             1244 |    27 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  741 |             1245 |    54 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  742 |             1246 |    44 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  743 |             1249 |    29 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  744 |             1250 |    54 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  745 |             1251 |    31 | No          | Research & Development |           2 | Medical          |               1 |
|  746 |             1252 |    31 | No          | Research & Development |           3 | Medical          |               1 |
|  747 |             1254 |    59 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  748 |             1255 |    43 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  749 |             1256 |    49 | No          | Research & Development |           2 | Medical          |               1 |
|  750 |             1257 |    36 | No          | Research & Development |           3 | Technical Degree |               1 |
|  751 |             1258 |    48 | No          | Research & Development |           2 | Technical Degree |               1 |
|  752 |             1259 |    27 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  753 |             1260 |    29 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  754 |             1263 |    48 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  755 |             1264 |    29 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  756 |             1265 |    34 | No          | Research & Development |           3 | Technical Degree |               1 |
|  757 |             1267 |    44 | No          | Sales                  |           3 | Marketing        |               1 |
|  758 |             1268 |    33 | No          | Sales                  |           5 | Marketing        |               1 |
|  759 |             1269 |    19 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  760 |             1270 |    23 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  761 |             1275 |    26 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  762 |             1278 |    55 | No          | Research & Development |           1 | Medical          |               1 |
|  763 |             1280 |    46 | No          | Sales                  |           2 | Marketing        |               1 |
|  764 |             1281 |    34 | No          | Sales                  |           3 | Marketing        |               1 |
|  765 |             1282 |    51 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  766 |             1283 |    59 | No          | Research & Development |           4 | Medical          |               1 |
|  767 |             1285 |    34 | No          | Research & Development |           3 | Medical          |               1 |
|  768 |             1286 |    28 | No          | Research & Development |           4 | Medical          |               1 |
|  769 |             1288 |    44 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  770 |             1289 |    34 | No          | Human Resources        |           3 | Life Sciences    |               1 |
|  771 |             1291 |    35 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  772 |             1292 |    42 | No          | Research & Development |           4 | Medical          |               1 |
|  773 |             1293 |    43 | No          | Sales                  |           4 | Marketing        |               1 |
|  774 |             1294 |    36 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  775 |             1296 |    28 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  776 |             1297 |    51 | No          | Research & Development |           2 | Medical          |               1 |
|  777 |             1298 |    30 | No          | Research & Development |           2 | Medical          |               1 |
|  778 |             1301 |    28 | No          | Research & Development |           3 | Technical Degree |               1 |
|  779 |             1303 |    25 | No          | Research & Development |           3 | Medical          |               1 |
|  780 |             1304 |    32 | No          | Sales                  |           3 | Medical          |               1 |
|  781 |             1306 |    45 | No          | Research & Development |           3 | Medical          |               1 |
|  782 |             1307 |    39 | No          | Research & Development |           4 | Medical          |               1 |
|  783 |             1308 |    58 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  784 |             1311 |    30 | No          | Research & Development |           3 | Technical Degree |               1 |
|  785 |             1312 |    36 | No          | Research & Development |           4 | Technical Degree |               1 |
|  786 |             1314 |    46 | No          | Human Resources        |           2 | Life Sciences    |               1 |
|  787 |             1315 |    28 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  788 |             1317 |    50 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  789 |             1321 |    30 | No          | Research & Development |           4 | Medical          |               1 |
|  790 |             1322 |    39 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  791 |             1324 |    31 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  792 |             1329 |    41 | No          | Sales                  |           2 | Medical          |               1 |
|  793 |             1334 |    42 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  794 |             1336 |    55 | No          | Research & Development |           2 | Medical          |               1 |
|  795 |             1338 |    56 | No          | Human Resources        |           4 | Life Sciences    |               1 |
|  796 |             1340 |    40 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  797 |             1344 |    34 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  798 |             1346 |    40 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  799 |             1349 |    41 | No          | Sales                  |           3 | Marketing        |               1 |
|  800 |             1350 |    35 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  801 |             1352 |    51 | No          | Human Resources        |           3 | Life Sciences    |               1 |
|  802 |             1355 |    38 | No          | Sales                  |           2 | Life Sciences    |               1 |
|  803 |             1356 |    34 | No          | Sales                  |           2 | Medical          |               1 |
|  804 |             1358 |    25 | No          | Research & Development |           1 | Medical          |               1 |
|  805 |             1361 |    40 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  806 |             1362 |    36 | No          | Sales                  |           3 | Marketing        |               1 |
|  807 |             1363 |    48 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  808 |             1364 |    27 | No          | Sales                  |           3 | Medical          |               1 |
|  809 |             1367 |    51 | No          | Research & Development |           2 | Technical Degree |               1 |
|  810 |             1368 |    18 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  811 |             1369 |    35 | No          | Research & Development |           3 | Medical          |               1 |
|  812 |             1371 |    27 | No          | Sales                  |           1 | Life Sciences    |               1 |
|  813 |             1373 |    56 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  814 |             1374 |    34 | No          | Research & Development |           1 | Technical Degree |               1 |
|  815 |             1375 |    40 | No          | Research & Development |           1 | Medical          |               1 |
|  816 |             1377 |    34 | No          | Research & Development |           3 | Medical          |               1 |
|  817 |             1382 |    38 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  818 |             1383 |    34 | No          | Research & Development |           4 | Technical Degree |               1 |
|  819 |             1387 |    28 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  820 |             1390 |    39 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  821 |             1391 |    51 | No          | Sales                  |           3 | Marketing        |               1 |
|  822 |             1392 |    41 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  823 |             1394 |    37 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  824 |             1395 |    33 | No          | Sales                  |           1 | Life Sciences    |               1 |
|  825 |             1396 |    32 | No          | Sales                  |           1 | Marketing        |               1 |
|  826 |             1397 |    39 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  827 |             1399 |    25 | No          | Sales                  |           1 | Life Sciences    |               1 |
|  828 |             1401 |    52 | No          | Research & Development |           2 | Medical          |               1 |
|  829 |             1402 |    43 | No          | Research & Development |           3 | Medical          |               1 |
|  830 |             1403 |    27 | No          | Sales                  |           3 | Marketing        |               1 |
|  831 |             1407 |    26 | No          | Research & Development |           1 | Medical          |               1 |
|  832 |             1408 |    42 | No          | Human Resources        |           3 | Human Resources  |               1 |
|  833 |             1409 |    52 | No          | Research & Development |           4 | Other            |               1 |
|  834 |             1411 |    37 | No          | Research & Development |           3 | Medical          |               1 |
|  835 |             1412 |    35 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  836 |             1415 |    25 | No          | Research & Development |           3 | Technical Degree |               1 |
|  837 |             1417 |    26 | No          | Research & Development |           3 | Other            |               1 |
|  838 |             1419 |    29 | No          | Human Resources        |           3 | Other            |               1 |
|  839 |             1422 |    54 | No          | Research & Development |           3 | Medical          |               1 |
|  840 |             1423 |    58 | No          | Research & Development |           3 | Medical          |               1 |
|  841 |             1424 |    55 | No          | Research & Development |           4 | Medical          |               1 |
|  842 |             1425 |    36 | No          | Sales                  |           4 | Marketing        |               1 |
|  843 |             1428 |    30 | No          | Sales                  |           4 | Marketing        |               1 |
|  844 |             1430 |    31 | No          | Research & Development |           5 | Life Sciences    |               1 |
|  845 |             1431 |    34 | No          | Research & Development |           4 | Other            |               1 |
|  846 |             1434 |    27 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  847 |             1435 |    36 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  848 |             1436 |    36 | No          | Sales                  |           4 | Marketing        |               1 |
|  849 |             1438 |    47 | No          | Research & Development |           3 | Technical Degree |               1 |
|  850 |             1440 |    37 | No          | Research & Development |           2 | Technical Degree |               1 |
|  851 |             1441 |    56 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  852 |             1443 |    47 | No          | Research & Development |           4 | Medical          |               1 |
|  853 |             1445 |    24 | No          | Sales                  |           1 | Medical          |               1 |
|  854 |             1446 |    32 | No          | Sales                  |           5 | Marketing        |               1 |
|  855 |             1447 |    34 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  856 |             1448 |    41 | No          | Research & Development |           5 | Medical          |               1 |
|  857 |             1449 |    40 | No          | Research & Development |           4 | Other            |               1 |
|  858 |             1453 |    31 | No          | Sales                  |           2 | Life Sciences    |               1 |
|  859 |             1460 |    45 | No          | Research & Development |           3 | Medical          |               1 |
|  860 |             1461 |    31 | No          | Human Resources        |           2 | Medical          |               1 |
|  861 |             1465 |    45 | No          | Research & Development |           3 | Technical Degree |               1 |
|  862 |             1466 |    48 | No          | Sales                  |           3 | Marketing        |               1 |
|  863 |             1468 |    40 | No          | Research & Development |           1 | Medical          |               1 |
|  864 |             1469 |    28 | No          | Sales                  |           3 | Medical          |               1 |
|  865 |             1471 |    44 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  866 |             1472 |    53 | No          | Research & Development |           3 | Medical          |               1 |
|  867 |             1473 |    49 | No          | Research & Development |           4 | Technical Degree |               1 |
|  868 |             1474 |    40 | No          | Research & Development |           3 | Medical          |               1 |
|  869 |             1475 |    44 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  870 |             1477 |    33 | No          | Sales                  |           3 | Medical          |               1 |
|  871 |             1478 |    34 | No          | Sales                  |           3 | Other            |               1 |
|  872 |             1479 |    30 | No          | Sales                  |           1 | Life Sciences    |               1 |
|  873 |             1480 |    42 | No          | Research & Development |           2 | Medical          |               1 |
|  874 |             1481 |    44 | No          | Sales                  |           5 | Marketing        |               1 |
|  875 |             1482 |    30 | No          | Research & Development |           3 | Technical Degree |               1 |
|  876 |             1483 |    57 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  877 |             1484 |    49 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  878 |             1485 |    34 | No          | Research & Development |           3 | Medical          |               1 |
|  879 |             1492 |    35 | No          | Sales                  |           1 | Life Sciences    |               1 |
|  880 |             1495 |    24 | No          | Sales                  |           2 | Life Sciences    |               1 |
|  881 |             1496 |    44 | No          | Research & Development |           1 | Medical          |               1 |
|  882 |             1497 |    29 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  883 |             1499 |    30 | No          | Human Resources        |           3 | Life Sciences    |               1 |
|  884 |             1501 |    55 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  885 |             1502 |    33 | No          | Research & Development |           4 | Medical          |               1 |
|  886 |             1503 |    47 | No          | Sales                  |           3 | Medical          |               1 |
|  887 |             1506 |    28 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  888 |             1507 |    28 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  889 |             1509 |    49 | No          | Research & Development |           2 | Medical          |               1 |
|  890 |             1513 |    29 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  891 |             1514 |    28 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  892 |             1515 |    33 | No          | Research & Development |           5 | Life Sciences    |               1 |
|  893 |             1516 |    32 | No          | Research & Development |           3 | Medical          |               1 |
|  894 |             1520 |    54 | No          | Research & Development |           4 | Medical          |               1 |
|  895 |             1523 |    44 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  896 |             1525 |    39 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  897 |             1527 |    46 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  898 |             1529 |    35 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  899 |             1533 |    23 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  900 |             1535 |    34 | No          | Sales                  |           3 | Technical Degree |               1 |
|  901 |             1539 |    50 | No          | Research & Development |           5 | Medical          |               1 |
|  902 |             1541 |    34 | No          | Sales                  |           2 | Technical Degree |               1 |
|  903 |             1542 |    42 | No          | Research & Development |           3 | Medical          |               1 |
|  904 |             1543 |    37 | No          | Research & Development |           3 | Medical          |               1 |
|  905 |             1544 |    29 | No          | Research & Development |           1 | Other            |               1 |
|  906 |             1545 |    33 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  907 |             1546 |    45 | No          | Research & Development |           3 | Technical Degree |               1 |
|  908 |             1547 |    42 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  909 |             1548 |    40 | No          | Sales                  |           2 | Medical          |               1 |
|  910 |             1549 |    33 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  911 |             1550 |    40 | No          | Human Resources        |           2 | Medical          |               1 |
|  912 |             1551 |    24 | No          | Research & Development |           2 | Technical Degree |               1 |
|  913 |             1552 |    40 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  914 |             1553 |    45 | No          | Research & Development |           4 | Technical Degree |               1 |
|  915 |             1554 |    35 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  916 |             1555 |    32 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  917 |             1556 |    36 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  918 |             1557 |    48 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  919 |             1558 |    29 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  920 |             1560 |    33 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  921 |             1563 |    38 | No          | Human Resources        |           4 | Human Resources  |               1 |
|  922 |             1564 |    35 | No          | Research & Development |           3 | Medical          |               1 |
|  923 |             1568 |    30 | No          | Sales                  |           4 | Technical Degree |               1 |
|  924 |             1574 |    32 | No          | Research & Development |           4 | Technical Degree |               1 |
|  925 |             1576 |    48 | No          | Research & Development |           4 | Other            |               1 |
|  926 |             1577 |    34 | No          | Research & Development |           4 | Medical          |               1 |
|  927 |             1578 |    55 | No          | Sales                  |           5 | Marketing        |               1 |
|  928 |             1580 |    34 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  929 |             1581 |    26 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  930 |             1582 |    38 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  931 |             1583 |    38 | No          | Sales                  |           3 | Life Sciences    |               1 |
|  932 |             1585 |    36 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  933 |             1586 |    29 | No          | Research & Development |           1 | Medical          |               1 |
|  934 |             1587 |    35 | No          | Research & Development |           4 | Medical          |               1 |
|  935 |             1588 |    39 | No          | Sales                  |           3 | Medical          |               1 |
|  936 |             1590 |    29 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  937 |             1591 |    50 | No          | Sales                  |           3 | Marketing        |               1 |
|  938 |             1592 |    23 | No          | Research & Development |           3 | Technical Degree |               1 |
|  939 |             1594 |    36 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  940 |             1595 |    42 | No          | Research & Development |           2 | Other            |               1 |
|  941 |             1596 |    35 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  942 |             1597 |    34 | No          | Research & Development |           4 | Technical Degree |               1 |
|  943 |             1598 |    40 | No          | Sales                  |           2 | Life Sciences    |               1 |
|  944 |             1599 |    43 | No          | Research & Development |           3 | Technical Degree |               1 |
|  945 |             1601 |    35 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  946 |             1602 |    46 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  947 |             1605 |    22 | No          | Research & Development |           2 | Other            |               1 |
|  948 |             1606 |    50 | No          | Research & Development |           5 | Medical          |               1 |
|  949 |             1607 |    32 | No          | Research & Development |           4 | Other            |               1 |
|  950 |             1608 |    44 | No          | Research & Development |           3 | Medical          |               1 |
|  951 |             1609 |    30 | No          | Research & Development |           3 | Medical          |               1 |
|  952 |             1611 |    45 | No          | Research & Development |           5 | Medical          |               1 |
|  953 |             1612 |    45 | No          | Sales                  |           3 | Marketing        |               1 |
|  954 |             1613 |    31 | No          | Sales                  |           4 | Other            |               1 |
|  955 |             1614 |    36 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  956 |             1615 |    34 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  957 |             1617 |    49 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  958 |             1618 |    39 | No          | Research & Development |           5 | Medical          |               1 |
|  959 |             1619 |    27 | No          | Research & Development |           3 | Other            |               1 |
|  960 |             1621 |    35 | No          | Research & Development |           5 | Life Sciences    |               1 |
|  961 |             1622 |    28 | No          | Research & Development |           3 | Medical          |               1 |
|  962 |             1623 |    21 | No          | Research & Development |           1 | Medical          |               1 |
|  963 |             1625 |    47 | No          | Human Resources        |           4 | Life Sciences    |               1 |
|  964 |             1627 |    39 | No          | Research & Development |           2 | Medical          |               1 |
|  965 |             1628 |    40 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  966 |             1630 |    35 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  967 |             1631 |    37 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  968 |             1633 |    39 | No          | Research & Development |           3 | Medical          |               1 |
|  969 |             1635 |    45 | No          | Research & Development |           2 | Other            |               1 |
|  970 |             1638 |    38 | No          | Research & Development |           2 | Medical          |               1 |
|  971 |             1640 |    37 | No          | Research & Development |           3 | Medical          |               1 |
|  972 |             1641 |    40 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  973 |             1642 |    44 | No          | Human Resources        |           5 | Human Resources  |               1 |
|  974 |             1644 |    48 | No          | Research & Development |           5 | Medical          |               1 |
|  975 |             1646 |    24 | No          | Research & Development |           1 | Technical Degree |               1 |
|  976 |             1647 |    27 | No          | Research & Development |           3 | Medical          |               1 |
|  977 |             1648 |    27 | No          | Research & Development |           3 | Medical          |               1 |
|  978 |             1650 |    29 | No          | Sales                  |           3 | Medical          |               1 |
|  979 |             1651 |    36 | No          | Research & Development |           4 | Life Sciences    |               1 |
|  980 |             1653 |    25 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  981 |             1654 |    39 | No          | Research & Development |           3 | Medical          |               1 |
|  982 |             1655 |    49 | No          | Research & Development |           4 | Other            |               1 |
|  983 |             1656 |    50 | No          | Research & Development |           5 | Life Sciences    |               1 |
|  984 |             1657 |    20 | No          | Sales                  |           3 | Medical          |               1 |
|  985 |             1658 |    34 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  986 |             1659 |    36 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  987 |             1661 |    49 | No          | Research & Development |           1 | Life Sciences    |               1 |
|  988 |             1662 |    36 | No          | Research & Development |           4 | Medical          |               1 |
|  989 |             1664 |    36 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  990 |             1665 |    54 | No          | Research & Development |           5 | Medical          |               1 |
|  991 |             1666 |    43 | No          | Research & Development |           2 | Life Sciences    |               1 |
|  992 |             1668 |    38 | No          | Research & Development |           3 | Life Sciences    |               1 |
|  993 |             1669 |    29 | No          | Sales                  |           3 | Medical          |               1 |
|  994 |             1670 |    33 | No          | Sales                  |           4 | Medical          |               1 |
|  995 |             1671 |    32 | No          | Research & Development |           3 | Medical          |               1 |
|  996 |             1673 |    31 | No          | Sales                  |           4 | Life Sciences    |               1 |
|  997 |             1674 |    49 | No          | Research & Development |           3 | Medical          |               1 |
|  998 |             1675 |    38 | No          | Research & Development |           3 | Medical          |               1 |
|  999 |             1676 |    47 | No          | Sales                  |           4 | Life Sciences    |               1 |
| 1000 |             1677 |    49 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1001 |             1678 |    41 | No          | Sales                  |           2 | Life Sciences    |               1 |
| 1002 |             1680 |    20 | No          | Sales                  |           1 | Life Sciences    |               1 |
| 1003 |             1681 |    33 | No          | Sales                  |           3 | Life Sciences    |               1 |
| 1004 |             1682 |    36 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1005 |             1683 |    44 | No          | Human Resources        |           3 | Life Sciences    |               1 |
| 1006 |             1687 |    38 | No          | Research & Development |           2 | Medical          |               1 |
| 1007 |             1689 |    53 | No          | Research & Development |           4 | Medical          |               1 |
| 1008 |             1693 |    26 | No          | Research & Development |           3 | Medical          |               1 |
| 1009 |             1694 |    55 | No          | Research & Development |           3 | Technical Degree |               1 |
| 1010 |             1696 |    34 | No          | Research & Development |           2 | Medical          |               1 |
| 1011 |             1697 |    60 | No          | Research & Development |           4 | Medical          |               1 |
| 1012 |             1698 |    33 | No          | Research & Development |           3 | Medical          |               1 |
| 1013 |             1700 |    37 | No          | Sales                  |           4 | Medical          |               1 |
| 1014 |             1701 |    34 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1015 |             1703 |    44 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1016 |             1704 |    35 | No          | Research & Development |           4 | Medical          |               1 |
| 1017 |             1706 |    43 | No          | Sales                  |           3 | Medical          |               1 |
| 1018 |             1707 |    24 | No          | Research & Development |           3 | Medical          |               1 |
| 1019 |             1708 |    41 | No          | Sales                  |           3 | Marketing        |               1 |
| 1020 |             1709 |    29 | No          | Research & Development |           4 | Medical          |               1 |
| 1021 |             1710 |    36 | No          | Sales                  |           4 | Life Sciences    |               1 |
| 1022 |             1712 |    45 | No          | Research & Development |           1 | Life Sciences    |               1 |
| 1023 |             1718 |    26 | No          | Research & Development |           4 | Medical          |               1 |
| 1024 |             1719 |    45 | No          | Research & Development |           2 | Technical Degree |               1 |
| 1025 |             1720 |    32 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1026 |             1721 |    31 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1027 |             1722 |    41 | No          | Human Resources        |           3 | Human Resources  |               1 |
| 1028 |             1724 |    40 | No          | Research & Development |           2 | Life Sciences    |               1 |
| 1029 |             1725 |    24 | No          | Research & Development |           1 | Medical          |               1 |
| 1030 |             1727 |    46 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1031 |             1728 |    35 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1032 |             1729 |    30 | No          | Research & Development |           1 | Life Sciences    |               1 |
| 1033 |             1731 |    47 | No          | Sales                  |           4 | Marketing        |               1 |
| 1034 |             1732 |    46 | No          | Sales                  |           3 | Life Sciences    |               1 |
| 1035 |             1735 |    23 | No          | Research & Development |           1 | Medical          |               1 |
| 1036 |             1736 |    31 | No          | Research & Development |           1 | Technical Degree |               1 |
| 1037 |             1737 |    39 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1038 |             1739 |    32 | No          | Sales                  |           3 | Life Sciences    |               1 |
| 1039 |             1740 |    40 | No          | Sales                  |           4 | Medical          |               1 |
| 1040 |             1744 |    45 | No          | Human Resources        |           3 | Life Sciences    |               1 |
| 1041 |             1745 |    30 | No          | Research & Development |           4 | Technical Degree |               1 |
| 1042 |             1746 |    24 | No          | Human Resources        |           3 | Medical          |               1 |
| 1043 |             1749 |    31 | No          | Sales                  |           3 | Technical Degree |               1 |
| 1044 |             1751 |    27 | No          | Research & Development |           3 | Medical          |               1 |
| 1045 |             1753 |    29 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1046 |             1754 |    30 | No          | Sales                  |           2 | Marketing        |               1 |
| 1047 |             1755 |    34 | No          | Research & Development |           4 | Medical          |               1 |
| 1048 |             1756 |    33 | No          | Sales                  |           3 | Marketing        |               1 |
| 1049 |             1757 |    49 | No          | Sales                  |           4 | Marketing        |               1 |
| 1050 |             1760 |    38 | No          | Research & Development |           2 | Medical          |               1 |
| 1051 |             1762 |    29 | No          | Research & Development |           3 | Technical Degree |               1 |
| 1052 |             1763 |    30 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1053 |             1764 |    32 | No          | Research & Development |           4 | Technical Degree |               1 |
| 1054 |             1766 |    38 | No          | Research & Development |           3 | Medical          |               1 |
| 1055 |             1768 |    42 | No          | Research & Development |           3 | Medical          |               1 |
| 1056 |             1770 |    55 | No          | Research & Development |           3 | Medical          |               1 |
| 1057 |             1771 |    33 | No          | Research & Development |           3 | Technical Degree |               1 |
| 1058 |             1772 |    41 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1059 |             1774 |    34 | No          | Sales                  |           3 | Life Sciences    |               1 |
| 1060 |             1775 |    53 | No          | Research & Development |           4 | Medical          |               1 |
| 1061 |             1778 |    43 | No          | Human Resources        |           3 | Life Sciences    |               1 |
| 1062 |             1779 |    34 | No          | Sales                  |           2 | Life Sciences    |               1 |
| 1063 |             1782 |    38 | No          | Research & Development |           2 | Other            |               1 |
| 1064 |             1784 |    31 | No          | Sales                  |           4 | Marketing        |               1 |
| 1065 |             1786 |    51 | No          | Research & Development |           3 | Technical Degree |               1 |
| 1066 |             1787 |    37 | No          | Sales                  |           2 | Marketing        |               1 |
| 1067 |             1789 |    46 | No          | Research & Development |           4 | Medical          |               1 |
| 1068 |             1790 |    36 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1069 |             1794 |    37 | No          | Human Resources        |           2 | Other            |               1 |
| 1070 |             1798 |    33 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1071 |             1799 |    28 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1072 |             1800 |    39 | No          | Research & Development |           1 | Medical          |               1 |
| 1073 |             1801 |    46 | No          | Sales                  |           2 | Life Sciences    |               1 |
| 1074 |             1802 |    40 | No          | Research & Development |           2 | Life Sciences    |               1 |
| 1075 |             1803 |    42 | No          | Research & Development |           3 | Medical          |               1 |
| 1076 |             1804 |    35 | No          | Research & Development |           2 | Medical          |               1 |
| 1077 |             1805 |    38 | No          | Human Resources        |           3 | Human Resources  |               1 |
| 1078 |             1812 |    39 | No          | Sales                  |           3 | Life Sciences    |               1 |
| 1079 |             1813 |    43 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1080 |             1814 |    41 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1081 |             1815 |    41 | No          | Sales                  |           1 | Marketing        |               1 |
| 1082 |             1816 |    30 | No          | Research & Development |           3 | Medical          |               1 |
| 1083 |             1822 |    40 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1084 |             1823 |    34 | No          | Sales                  |           2 | Technical Degree |               1 |
| 1085 |             1824 |    58 | No          | Sales                  |           3 | Medical          |               1 |
| 1086 |             1826 |    35 | No          | Research & Development |           4 | Medical          |               1 |
| 1087 |             1827 |    47 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1088 |             1829 |    40 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1089 |             1830 |    54 | No          | Research & Development |           4 | Medical          |               1 |
| 1090 |             1833 |    31 | No          | Sales                  |           4 | Marketing        |               1 |
| 1091 |             1834 |    28 | No          | Research & Development |           3 | Medical          |               1 |
| 1092 |             1835 |    38 | No          | Sales                  |           4 | Marketing        |               1 |
| 1093 |             1836 |    26 | No          | Sales                  |           3 | Medical          |               1 |
| 1094 |             1837 |    58 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1095 |             1839 |    18 | No          | Research & Development |           3 | Medical          |               1 |
| 1096 |             1845 |    45 | No          | Sales                  |           4 | Life Sciences    |               1 |
| 1097 |             1847 |    36 | No          | Research & Development |           4 | Other            |               1 |
| 1098 |             1849 |    43 | No          | Sales                  |           4 | Life Sciences    |               1 |
| 1099 |             1850 |    27 | No          | Research & Development |           2 | Life Sciences    |               1 |
| 1100 |             1852 |    29 | No          | Research & Development |           1 | Medical          |               1 |
| 1101 |             1853 |    32 | No          | Sales                  |           4 | Marketing        |               1 |
| 1102 |             1854 |    42 | No          | Research & Development |           4 | Technical Degree |               1 |
| 1103 |             1856 |    47 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1104 |             1857 |    46 | No          | Research & Development |           2 | Life Sciences    |               1 |
| 1105 |             1858 |    28 | No          | Human Resources        |           2 | Life Sciences    |               1 |
| 1106 |             1859 |    29 | No          | Research & Development |           1 | Life Sciences    |               1 |
| 1107 |             1860 |    42 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1108 |             1863 |    46 | No          | Sales                  |           3 | Technical Degree |               1 |
| 1109 |             1864 |    27 | No          | Sales                  |           1 | Medical          |               1 |
| 1110 |             1865 |    29 | No          | Human Resources        |           1 | Medical          |               1 |
| 1111 |             1866 |    43 | No          | Research & Development |           3 | Medical          |               1 |
| 1112 |             1867 |    48 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1113 |             1870 |    27 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1114 |             1871 |    39 | No          | Research & Development |           4 | Other            |               1 |
| 1115 |             1873 |    55 | No          | Research & Development |           4 | Technical Degree |               1 |
| 1116 |             1875 |    28 | No          | Sales                  |           3 | Medical          |               1 |
| 1117 |             1880 |    36 | No          | Sales                  |           4 | Technical Degree |               1 |
| 1118 |             1881 |    31 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1119 |             1882 |    34 | No          | Sales                  |           3 | Life Sciences    |               1 |
| 1120 |             1883 |    29 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1121 |             1885 |    37 | No          | Research & Development |           4 | Medical          |               1 |
| 1122 |             1886 |    35 | No          | Research & Development |           2 | Other            |               1 |
| 1123 |             1888 |    45 | No          | Research & Development |           2 | Life Sciences    |               1 |
| 1124 |             1890 |    36 | No          | Human Resources        |           1 | Human Resources  |               1 |
| 1125 |             1892 |    40 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1126 |             1893 |    26 | No          | Research & Development |           2 | Life Sciences    |               1 |
| 1127 |             1898 |    27 | No          | Sales                  |           2 | Medical          |               1 |
| 1128 |             1900 |    48 | No          | Research & Development |           3 | Medical          |               1 |
| 1129 |             1903 |    44 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1130 |             1908 |    36 | No          | Sales                  |           2 | Marketing        |               1 |
| 1131 |             1909 |    41 | No          | Sales                  |           3 | Marketing        |               1 |
| 1132 |             1911 |    42 | No          | Research & Development |           3 | Medical          |               1 |
| 1133 |             1912 |    31 | No          | Sales                  |           2 | Medical          |               1 |
| 1134 |             1915 |    34 | No          | Sales                  |           1 | Medical          |               1 |
| 1135 |             1916 |    31 | No          | Research & Development |           3 | Medical          |               1 |
| 1136 |             1918 |    26 | No          | Research & Development |           3 | Other            |               1 |
| 1137 |             1922 |    45 | No          | Research & Development |           4 | Medical          |               1 |
| 1138 |             1924 |    33 | No          | Sales                  |           4 | Marketing        |               1 |
| 1139 |             1927 |    28 | No          | Sales                  |           2 | Life Sciences    |               1 |
| 1140 |             1929 |    39 | No          | Sales                  |           4 | Life Sciences    |               1 |
| 1141 |             1931 |    27 | No          | Research & Development |           4 | Technical Degree |               1 |
| 1142 |             1932 |    34 | No          | Research & Development |           4 | Other            |               1 |
| 1143 |             1934 |    47 | No          | Research & Development |           4 | Technical Degree |               1 |
| 1144 |             1935 |    56 | No          | Sales                  |           5 | Marketing        |               1 |
| 1145 |             1936 |    39 | No          | Research & Development |           2 | Medical          |               1 |
| 1146 |             1937 |    38 | No          | Research & Development |           3 | Medical          |               1 |
| 1147 |             1938 |    58 | No          | Sales                  |           3 | Life Sciences    |               1 |
| 1148 |             1940 |    38 | No          | Research & Development |           2 | Life Sciences    |               1 |
| 1149 |             1941 |    49 | No          | Research & Development |           1 | Life Sciences    |               1 |
| 1150 |             1943 |    42 | No          | Sales                  |           4 | Marketing        |               1 |
| 1151 |             1945 |    35 | No          | Sales                  |           4 | Medical          |               1 |
| 1152 |             1947 |    28 | No          | Research & Development |           3 | Medical          |               1 |
| 1153 |             1948 |    31 | No          | Research & Development |           2 | Medical          |               1 |
| 1154 |             1949 |    36 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1155 |             1950 |    34 | No          | Sales                  |           3 | Marketing        |               1 |
| 1156 |             1951 |    34 | No          | Sales                  |           4 | Medical          |               1 |
| 1157 |             1952 |    26 | No          | Research & Development |           3 | Medical          |               1 |
| 1158 |             1954 |    29 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1159 |             1955 |    32 | No          | Research & Development |           4 | Medical          |               1 |
| 1160 |             1956 |    31 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1161 |             1961 |    38 | No          | Sales                  |           3 | Life Sciences    |               1 |
| 1162 |             1962 |    35 | No          | Sales                  |           4 | Life Sciences    |               1 |
| 1163 |             1965 |    27 | No          | Sales                  |           3 | Marketing        |               1 |
| 1164 |             1966 |    32 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1165 |             1969 |    54 | No          | Research & Development |           2 | Life Sciences    |               1 |
| 1166 |             1970 |    33 | No          | Research & Development |           2 | Life Sciences    |               1 |
| 1167 |             1971 |    43 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1168 |             1972 |    38 | No          | Human Resources        |           4 | Other            |               1 |
| 1169 |             1973 |    55 | No          | Human Resources        |           4 | Human Resources  |               1 |
| 1170 |             1974 |    31 | No          | Research & Development |           1 | Medical          |               1 |
| 1171 |             1975 |    39 | No          | Sales                  |           4 | Marketing        |               1 |
| 1172 |             1976 |    42 | No          | Research & Development |           2 | Life Sciences    |               1 |
| 1173 |             1979 |    31 | No          | Research & Development |           3 | Medical          |               1 |
| 1174 |             1980 |    54 | No          | Research & Development |           3 | Medical          |               1 |
| 1175 |             1981 |    24 | No          | Research & Development |           2 | Life Sciences    |               1 |
| 1176 |             1982 |    23 | No          | Research & Development |           2 | Other            |               1 |
| 1177 |             1985 |    40 | No          | Research & Development |           3 | Technical Degree |               1 |
| 1178 |             1986 |    40 | No          | Sales                  |           2 | Marketing        |               1 |
| 1179 |             1987 |    25 | No          | Human Resources        |           3 | Human Resources  |               1 |
| 1180 |             1989 |    30 | No          | Research & Development |           2 | Medical          |               1 |
| 1181 |             1992 |    25 | No          | Research & Development |           1 | Other            |               1 |
| 1182 |             1993 |    47 | No          | Research & Development |           3 | Medical          |               1 |
| 1183 |             1994 |    33 | No          | Research & Development |           2 | Medical          |               1 |
| 1184 |             1995 |    38 | No          | Sales                  |           4 | Life Sciences    |               1 |
| 1185 |             1996 |    31 | No          | Sales                  |           2 | Life Sciences    |               1 |
| 1186 |             1997 |    38 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1187 |             1998 |    42 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1188 |             1999 |    41 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1189 |             2000 |    47 | No          | Research & Development |           1 | Medical          |               1 |
| 1190 |             2003 |    35 | No          | Research & Development |           4 | Medical          |               1 |
| 1191 |             2007 |    22 | No          | Research & Development |           2 | Life Sciences    |               1 |
| 1192 |             2008 |    35 | No          | Research & Development |           4 | Medical          |               1 |
| 1193 |             2009 |    33 | No          | Research & Development |           2 | Medical          |               1 |
| 1194 |             2010 |    32 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1195 |             2012 |    40 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1196 |             2013 |    32 | No          | Sales                  |           4 | Medical          |               1 |
| 1197 |             2014 |    39 | No          | Research & Development |           1 | Life Sciences    |               1 |
| 1198 |             2015 |    38 | No          | Research & Development |           3 | Medical          |               1 |
| 1199 |             2016 |    32 | No          | Sales                  |           4 | Marketing        |               1 |
| 1200 |             2017 |    37 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1201 |             2018 |    25 | No          | Sales                  |           2 | Other            |               1 |
| 1202 |             2019 |    52 | No          | Sales                  |           4 | Life Sciences    |               1 |
| 1203 |             2020 |    44 | No          | Research & Development |           3 | Medical          |               1 |
| 1204 |             2021 |    21 | No          | Sales                  |           1 | Medical          |               1 |
| 1205 |             2022 |    39 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1206 |             2024 |    36 | No          | Sales                  |           3 | Medical          |               1 |
| 1207 |             2025 |    36 | No          | Research & Development |           2 | Life Sciences    |               1 |
| 1208 |             2026 |    56 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1209 |             2031 |    42 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1210 |             2034 |    41 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1211 |             2035 |    34 | No          | Sales                  |           3 | Marketing        |               1 |
| 1212 |             2036 |    36 | No          | Sales                  |           4 | Marketing        |               1 |
| 1213 |             2037 |    41 | No          | Sales                  |           3 | Life Sciences    |               1 |
| 1214 |             2038 |    32 | No          | Research & Development |           3 | Technical Degree |               1 |
| 1215 |             2040 |    35 | No          | Human Resources        |           4 | Life Sciences    |               1 |
| 1216 |             2041 |    38 | No          | Sales                  |           2 | Life Sciences    |               1 |
| 1217 |             2045 |    36 | No          | Sales                  |           4 | Marketing        |               1 |
| 1218 |             2046 |    45 | No          | Sales                  |           3 | Life Sciences    |               1 |
| 1219 |             2048 |    40 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1220 |             2049 |    35 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1221 |             2051 |    40 | No          | Research & Development |           4 | Medical          |               1 |
| 1222 |             2052 |    35 | No          | Research & Development |           4 | Life Sciences    |               1 |
| 1223 |             2053 |    29 | No          | Research & Development |           2 | Other            |               1 |
| 1224 |             2054 |    29 | No          | Research & Development |           4 | Medical          |               1 |
| 1225 |             2056 |    39 | No          | Sales                  |           1 | Marketing        |               1 |
| 1226 |             2057 |    31 | No          | Research & Development |           3 | Medical          |               1 |
| 1227 |             2060 |    26 | No          | Sales                  |           3 | Other            |               1 |
| 1228 |             2061 |    36 | No          | Research & Development |           2 | Medical          |               1 |
| 1229 |             2062 |    39 | No          | Research & Development |           1 | Medical          |               1 |
| 1230 |             2064 |    27 | No          | Research & Development |           3 | Life Sciences    |               1 |
| 1231 |             2065 |    49 | No          | Sales                  |           3 | Medical          |               1 |
| 1232 |             2068 |    34 | No          | Research & Development |           3 | Medical          |               1 |

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

