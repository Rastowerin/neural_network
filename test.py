import numpy
from keras.datasets import boston_housing
from keras.models import Sequential
from keras.layers import Dense
from generator import *

numpy.random.seed(42)

(x_train1, y_train1), (x_test1, y_test1) = boston_housing.load_data()


mean = x_test.mean(axis=0)
std = x_test.std(axis=0)

x_train -= mean
x_train /= std
x_test -= mean
x_test /= std

print(x_train.shape[1])

model = Sequential()
model.add(Dense(10, activation='relu', input_shape=(x_train.shape[1],)))
model.add(Dense(1))
model.compile(optimizer='adam', loss= 'mse', metrics=['mae'])

model.fit(x_train, y_train, epochs=10, batch_size=1, verbose=1)

mse, mae = model.evaluate(x_test, y_test, verbose=1)

pred = model.predict(x_test)
print(pred[1][0], y_test[1])
print(pred[5][0], y_test[5])
print(pred[10][0], y_test[10])