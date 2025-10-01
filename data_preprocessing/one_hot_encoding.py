# it is used for inputs X
# and it is used for nominal data
import pandas as pd

data = {
    "Country": ["India", "USA", "UK", "India", "USA"],
    "Gender": ["Male", "Female", "Female", "Male", "Male"],
    "Age": [22, 35, 29, 40, 30],
    "Salary": [20000, 40000, 35000, 30000, 30000],
    "Purchased": ["No", "Yes", "No", "Yes", "No"]
}

df_raw = pd.DataFrame(data)
df_encoded = pd.get_dummies(df_raw, columns=["Country","Gender"])

print(df_encoded)