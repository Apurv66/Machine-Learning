# train_test_split_data.py

import pandas as pd
from sklearn.model_selection import train_test_split

# Example dataset
data = {
    "Country": ["India", "USA", "UK", "India", "USA"],
    "Gender": ["Male", "Female", "Female", "Male", "Male"],
    "Age": [22, 35, 29, 40, 30],
    "Salary": [20000, 40000, 35000, 30000, 30000],
    "Purchased": ["No", "Yes", "No", "Yes", "No"]
}

df = pd.DataFrame(data)

X = df.drop("Purchased", axis=1)
y = df["Purchased"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training Features:\n", X_train)
print("\nTesting Features:\n", X_test)
print("\nTraining Labels:\n", y_train)
print("\nTesting Labels:\n", y_test)