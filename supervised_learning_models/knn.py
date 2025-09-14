import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Sleep_Hours": [8, 7, 6, 6, 5, 5, 4, 3],
    "Pass":        [0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Study_Hours", "Sleep_Hours"]].values
y = df["Pass"].values

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X, y)

study = 5
sleep = 6
pred = model.predict([[study,sleep]])

print(pred[0])