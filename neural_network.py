import numpy
from keras.models import Sequential
from keras.layers import Dense

numpy.random.seed(42)

def fit(x_train, x_test, y_train, y_test):
    model = Sequential()
    model.add(Dense(10, activation='relu', input_shape=(x_train.shape[1],)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss= 'mse', metrics=['mae'])

    model.fit(x_train, y_train, epochs=10, batch_size=1, verbose=1)

    mse, mae = model.evaluate(x_test, y_test, verbose=1)