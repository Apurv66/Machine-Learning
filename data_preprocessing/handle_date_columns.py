import pandas as pd

import pandas as pd

data = {
    'date': [
        "2023-01-15",
        "2023-05-22",
        "2023-09-10",
        "2024-02-28",
        "2024-07-04",
        "2024-11-19",
        "2025-03-05",
        "2025-06-12",
        "2025-08-30",
        "2025-12-25"],
    'value': [10, 25, 18, 30, 22, 15, 28, 35, 20, 40]
}

df = pd.DataFrame(data)

df['date'] = pd.to_datetime(df['date'])

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

print(df)