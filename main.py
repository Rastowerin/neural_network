import generator
import neural_network
import numpy as np


x_train = []
x_test = []
y_train = []
y_test = []
count = 0


for cicle in range(10000):
    if count < 5:
        x_train.append(a[:-1])
        y_train.append(a[-1:])
    else:
        x_test.append((a[:-1]))
        y_test.append(a[-1:])
        count = 0


x_train = np.array(x_train)
x_test = np.array(x_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

mean = x_test.mean(axis=0)
std = x_test.std(axis=0)

x_train -= mean
x_train /= std
x_test -= mean
x_test /= std

print(x_train)
print('===================================================================================================================================================')
print(x_test)
print('===================================================================================================================================================')
print(y_train)
print('===================================================================================================================================================')
print(y_test)

neural_network.fit(x_train, x_test, y_train, y_test)