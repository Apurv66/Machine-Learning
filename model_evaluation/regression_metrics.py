from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

actual = [100, 200, 300]
pred   = [90, 210, 290]

mae = mean_absolute_error(actual, pred)
mse = mean_squared_error(actual, pred)
rmse = mse ** 0.5
r2 = r2_score(actual, pred)

print(mae)
print(mse)
print(rmse)
print(r2)