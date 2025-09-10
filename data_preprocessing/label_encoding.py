import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    "Country": ["India", "USA", "UK", "India", "USA"],
    "Gender": ["Male", "Female", "Female", "Male", "Male"],
    "Age": [22, 35, 29, 40, 30],
    "Salary": [20000, 40000, 35000, 30000, 30000],
    "Purchased": ["No", "Yes", "No", "Yes", "No"]
}

df_raw = pd.DataFrame(data)
df_encoded = df_raw.copy()

columns = ["Country", "Gender", "Purchased"]
for col in columns:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df_encoded[col])

print(df_encoded)