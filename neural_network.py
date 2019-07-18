import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
from keras.callbacks import LearningRateScheduler
from keras.optimizers import SGD

np.random.seed(42)


sd=[]
class LossHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.losses = [1,1]

    def on_epoch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))
        sd.append(step_decay(len(self.losses)))
        print('lr:', step_decay(len(self.losses)))

def model_save(model):
    model_json = model.to_json()

    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights("model.h5")

def predict(x_test, y_test, model, number):
    pred = model.predict(x_test)
    print(pred[number], y_test[number])

def step_decay(losses):
    if float(2*np.sqrt(np.array(history.losses[-1])))<0.3:
        lrate=0.01*1/(1+0.1*len(history.losses))
        decay_rate=2e-6
        return lrate
    else:
        lrate=0.1
        return lrate

def create_model(x_train, x_test, y_train, y_test):
    model = Sequential()
    model.add(Dense(11, activation='relu', use_bias=True, input_shape=(x_train.shape[1],)))
    model.add(Dense(2, activation='relu', use_bias=True, input_shape=(x_train.shape[1],)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])

    model.fit(x_train, y_train, epochs=10, batch_size=1, verbose=1, callbacks=[history, lrate])

    predict(x_test, y_test, model, 1)
    predict(x_test, y_test, model, 5)
    predict(x_test, y_test, model, 10)

    mse, mae = model.evaluate(x_test, y_test, verbose=2)
    model_save(model)

def fit(x_train, x_test, y_train, y_test):
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("model.h5")
    loaded_model.compile(optimizer='adam', loss='mse', metrics=['mae'])

    predict(x_test, y_test, loaded_model, 1)
    predict(x_test, y_test, loaded_model, 5)
    predict(x_test, y_test, loaded_model, 10)

    loaded_model.fit(x_train, y_train, nb_epoch=10, batch_size=1, verbose=1, callbacks=[history, lrate])

    mse, mae = loaded_model.evaluate(x_test, y_test, verbose=2)

    model_save(loaded_model)


learning_rate = 0.1
decay_rate = 5e-6

#optimizer = SGD(lr=learning_rate, rho=0.9, epsilon=None, decay=decay_rate)

history=LossHistory()
lrate=LearningRateScheduler(step_decay)