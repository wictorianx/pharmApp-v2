


import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

regressor = RandomForestRegressor(n_estimators=100, random_state=0)

new_data = np.array([[1, 2, 3, 4, 5]])
predictions = regressor.predict(new_data)
print('Predictions:', predictions)