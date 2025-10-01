# it is used for input X
# and it is used for ordinal data

import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

data = {
    "Employee id": [1, 2, 3, 4, 5, 6],
    "Education": ["Diploma", "Masters", "Bachelors", "Bachelors", "Diploma", "Bachelors"],
    "Salary": [15000, 55000, 34000, 40000, 25000, 36000]
}

df = pd.DataFrame(data)

oe = OrdinalEncoder(categories=[["Diploma", "Bachelors", "Masters"]])

df["Education"] = oe.fit_transform(df[["Education"]])

print(df)
