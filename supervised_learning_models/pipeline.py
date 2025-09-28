import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

data = {
    "Age": [22, 25, 47, 52],
    "Salary": [20000, 32000, 58000, 72000],
    "Purchased": [0, 0, 1, 1]
}
df = pd.DataFrame(data)

x = df.drop(columns="Purchased").values
y = df['Purchased'].values

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

pipe.fit(x, y)

pred = pipe.predict([[30,40000]])
print(pred)