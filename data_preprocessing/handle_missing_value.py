import pandas as pd

data = {
    "name": ["jateen", "kishaan", "pravin", "govind", "mukesh", "nirmala"],
    "age": [28, 33, 38, 29, 35, 38],
    "salary": [45000, None, 50000, 60000, 48000, 55000],
    "performance_score": [93.5, 9.2, 94, 83.8, 89, 95.5]
}

df = pd.DataFrame(data)

# drop column or row which have missing value
"""
df.dropna(inplace=True)
print(df)
"""

# fill the missing value
df['salary'] = df['salary'].fillna(df['salary'].mean())
print(df)
