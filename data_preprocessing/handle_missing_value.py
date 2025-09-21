import pandas as pd

data = {
    "id": [1,2,3,4,5,6],
    "job title": ["Software Developer", "UI/UX Designer", None, "ML Engineer", "Software Developer", "Data Scientist"],
    "salary": [45000, None, 50000, 60000, 48000, 55000],
    "performance score": [93.5, None, 94, 83.8, 89, 95.5]
}

df = pd.DataFrame(data)
print(df.isna().sum()) # Find the missing values

# Drop messing values
# df.dropna(inplace=True)

# Fill the missing values
df["salary"] = df["salary"].fillna(df["salary"].mean())
df["job title"] = df["job title"].fillna(df["job title"].mode()[0])
df["performance score"] = df["performance score"].fillna(df["performance score"].mean())

print(df)