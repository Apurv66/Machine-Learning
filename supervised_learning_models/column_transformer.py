import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

data = {
    "Age": [22, 25, 47, 52],
    "Salary": [20000, 32000, 58000, 72000],
    "Gender": ["Male", "Female", "Female", "Male"],
    "Purchased": [0, 0, 1, 1]
}
df = pd.DataFrame(data)

x = df.drop(columns="Purchased")
y = df['Purchased']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

preprocessor = ColumnTransformer(
    transformers=[
        ('scaler', StandardScaler(), ["Age", "Salary"]),
        ('ecoder', OneHotEncoder(), ["Gender"])
    ]
)

pipe = Pipeline([
    ('preprocessor', preprocessor),
    ('model', LogisticRegression())
])

pipe.fit(x_train, y_train)

sample = pd.DataFrame([[22, 20000, "Male"]], columns=["Age", "Salary", "Gender"]) # pipeline take dataframe with column name.
print(pipe.predict(sample))