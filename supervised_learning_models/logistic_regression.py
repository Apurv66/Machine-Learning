import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Pass":  [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours"]].values
y = df["Pass"].values

model = LogisticRegression()

model.fit(X, y)

hours = 5
pred = model.predict([[hours]])

print(pred[0])