from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

actual = [1, 0, 1, 1, 0, 1, 0]
pred   = [1, 0, 1, 0, 0, 1, 1]

accuracy = accuracy_score(actual, pred)
precision = precision_score(actual, pred)
recall = recall_score(actual, pred)
f1 = f1_score(actual, pred)
confusion = confusion_matrix(actual, pred)

print(accuracy)
print(precision)
print(recall)
print(f1)
print(confusion)