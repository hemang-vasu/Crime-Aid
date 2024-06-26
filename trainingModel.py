import os
# Keep using Keras 2
os.environ['TF_USE_LEGACY_KERAS'] = '1'

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from keras import layers, models
from sklearn.preprocessing import LabelEncoder, StandardScaler
#import tf_keras

dataset_df = pd.read_csv("gTimesTwo.csv")
print(dataset_df.head(3))

train_data, test_data = train_test_split(dataset_df, test_size=0.4, random_state=42)
#temp = test_data
#print(temp.head(3))
# Preprocess input features
encoder = LabelEncoder()
train_data['AREA NAME'] = encoder.fit_transform(train_data['AREA NAME'])
train_data['DATE OCC'] = encoder.fit_transform(train_data['DATE OCC'])
test_data['AREA NAME'] = encoder.fit_transform(test_data['AREA NAME'])
test_data['DATE OCC'] = encoder.fit_transform(test_data['DATE OCC'])

scaler = StandardScaler()
train_data[['DATE OCC', 'TIME OCC', 'AREA NAME', 'LAT', 'LON']] = scaler.fit_transform(train_data[['DATE OCC', 'TIME OCC', 'AREA NAME', 'LAT', 'LON']])
test_data[['DATE OCC', 'TIME OCC', 'AREA NAME', 'LAT', 'LON']] = scaler.fit_transform(test_data[['DATE OCC', 'TIME OCC', 'AREA NAME', 'LAT', 'LON']])

model = models.Sequential([
    # Input layer with 3 input features
    layers.Dense(64, activation='relu', input_shape=(5,)),
    # Hidden layer with 32 units and ReLU activation
    layers.Dense(32, activation='relu'),
    layers.Dense(32, activation='relu'),
    # Output layer with 1 unit (regression problem)
    layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

model.fit(train_data[['DATE OCC', 'TIME OCC', 'AREA NAME', 'LAT', 'LON']], train_data['Total Score'], epochs=5)

#model.summary()

#GTIMESTHREE IS VALUES TO FIND IN THE FUTURE: ACTUAL PREDICTION

dataset_dfTwo = pd.read_csv("gTimesThree.csv")

test_data = dataset_dfTwo
temp = test_data

test_data = test_data.drop(columns=['Total Score'])
test_data['AREA NAME'] = encoder.fit_transform(test_data['AREA NAME'])
test_data['DATE OCC'] = encoder.fit_transform(test_data['DATE OCC'])
test_data[['DATE OCC', 'TIME OCC', 'AREA NAME', 'LAT', 'LON']] = scaler.fit_transform(test_data[['DATE OCC', 'TIME OCC', 'AREA NAME', 'LAT', 'LON']])
# Make predictions on the test data
print("Calculating Predictions: ")
predictions = model.predict(test_data)

# Assuming predictions is a 1D array or a column vector, convert it to a DataFrame
#predictions_df = pd.DataFrame(predictions, columns=['Total Score'])
temp['Total Score'] = predictions
# Optionally, if you have the actual target values (y_test), you can concatenate them with the predictions
# actual_values_df = pd.DataFrame(y_test, columns=['Actual_Value'])
# combined_df = pd.concat([predictions_df, actual_values_df], axis=1)

# Save the predictions to a CSV file
temp.to_csv('predictions.csv', index=False)
#print(temp.head(3))

#loss = model.evaluate(test_data[['DATE OCC', 'TIME OCC', 'AREA NAME']], test_data['Total Score'])
#print('Mean Squared Error on Test Data:', loss)