from parsing import *
import random


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
    a = []
    for x in used_elements:
        for y in x.values():
            element = y
            a.append(element)
    return used_elements

print(generation())