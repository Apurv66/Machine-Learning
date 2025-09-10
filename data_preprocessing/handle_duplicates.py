import pandas as pd

data = {
    "id": [101, 102, 103, 101, 104, 105, 102],
    "name": ["Alice", "Bob", "Charlie", "Alice", "David", "Eva", "Bob"],
    "department": ["HR", "Finance", "IT", "HR", "Marketing", "IT", "Finance"],
    "salary": [50000, 60000, 55000, 50000, 62000, 58000, 60000]
}

df = pd.DataFrame(data)

print(df.duplicated())

df.drop_duplicates(inplace=True)

print(df)