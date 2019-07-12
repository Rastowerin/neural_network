from parsing import *
import random
import numpy as np


def generation():
    used_elements = []
    for element in range(2):
        used_elements.append(elements[list(elements)[random.randint(0, len(elements) - 1)]])
        y = 0
        for x in used_elements[element].keys():
            y += 1
            if y == 2:
                z = x
        used_elements[element].setdefault('темпиратура', float(random.randint(-100, int(used_elements[element][z]))))
        y = 0
        for x in used_elements[element].keys():
            y += 1
            if y == 2:
                z = x
        used_elements[element].setdefault('масса', float(random.randint(1, 100)))
    final_temperature = (used_elements[0]['удельная теплоемкость']*used_elements[0]['масса']*used_elements[0]['темпиратура']
                       + used_elements[1]['удельная теплоемкость']*used_elements[1]['масса']*used_elements[1]['темпиратура'])\
                      / (used_elements[0]['удельная теплоемкость']*used_elements[0]['масса']
                       + used_elements[1]['удельная теплоемкость']*used_elements[1]['масса'])
    used_elements.append({'финальная темпиратупа': final_temperature})
    return used_elements


x_train = []
x_test = []
y_train = []
y_test = []
count = 0

for cicle in range(10000):
    count += 1
    a = []
    for x in generation():
        for y in x.values():
            element = y
            a.append(element)
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

print(x_train)
print('===================================================================================================================================================')
print(x_test)
print('===================================================================================================================================================')
print(y_train)
print('===================================================================================================================================================')
print(y_test)