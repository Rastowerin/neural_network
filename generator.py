from parsing import *
import random


def generation():
    indexing = lambda x, y: 5 * x + y
    used_elements = []
    for element in range(2):
        used_elements.extend(elements[list(elements)[random.randint(0, len(elements) - 1)]])
        used_elements.append(float(random.randint(-100, int(used_elements[indexing(element, 1)]))))
        used_elements.append(float(random.randint(1, 100)))
        parameter_x = 0
        parameter_y = 0
    for element_number in range(len(used_elements)//5):
        parameter_x += used_elements[indexing(element_number, 0)]*used_elements[indexing(element_number, 4)]*used_elements[indexing(element_number, 3)]
        parameter_y += used_elements[indexing(element_number, 0)]*used_elements[indexing(element_number, 4)]
    final_temperature = parameter_x/parameter_y
    used_elements.append(final_temperature)
    return used_elements