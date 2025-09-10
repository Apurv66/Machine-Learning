import pandas as pd
from sklearn.preprocessing import StandardScaler

data = {
    "Age": [22, 32, 35, 25, 36],
    "Salary": [20000, 35000, 42000, 23000, 40000]
}

df = pd.DataFrame(data)

scaler = StandardScaler()

df_scaled_array = scaler.fit_transform(df)

df_scaled = pd.DataFrame(df_scaled_array, columns=df.columns)

print(df_scaled)