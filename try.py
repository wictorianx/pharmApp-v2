import numpy as np
import statsmodels.api as sm

# Generate an example time series data as a basic array
data = np.array([198, 259, 228, 210, 201, 161, 77, 112, 235, 202, 188, 268])

# Split the data into training and testing sets
train_data = data[:11]
test_data = data[11:]

# Fit the ARIMA model on the training data
model = sm.tsa.ARIMA(train_data, order=(1,1,1))
fitted_model = model.fit()

# Use the model to make predictions on the testing data
predictions = fitted_model.forecast(len(test_data))

# Evaluate the performance of the model using appropriate metrics
mse = ((predictions - test_data) ** 2).mean()
print(mse)