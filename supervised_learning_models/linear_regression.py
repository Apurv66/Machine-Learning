import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Size": [850, 900, 1000, 1100, 1200],
    "Price": [100000, 115000, 130000, 150000, 170000]
}

df = pd.DataFrame(data)

X = df[["Size"]].values
y = df["Price"].values

model = LinearRegression()
model.fit(X, y)

size = 1000
pred = model.predict([[size]])
print(int(pred[0]))
