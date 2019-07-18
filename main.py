import numpy as np
import random
import generator
import neural_network


x_train = []
x_test = []
y_train = []
y_test = []
count = 0


for cicle in range(100000):
    data = generator.generation()
    answer = random.choice(data)
    data[data.index(answer)] = 0
    while len(data) != 11:
        data.append(0)
    if count != 5:
        x_train.append(data)
        y_train.append(answer)
        count += 1
    else:
        x_test.append(data)
        y_test.append(answer)
        count = 0


x_train = np.array(x_train)
x_test = np.array(x_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

mean = x_train.mean(axis=0)
std = x_train.std(axis=0)

x_train -= mean
x_train /= std
x_test -= mean
x_test /= std

#print(x_train)
#print('===================================================================================================================================================')
#print(x_test)
#print('===================================================================================================================================================')
#print(y_train)
#print('===================================================================================================================================================')
#print(y_test)

#neural_network.create_model(x_train, x_test, y_train, y_test)
while True:
    neural_network.fit(x_train, x_test, y_train, y_test)