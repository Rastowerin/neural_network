from parsing import *
import random
used_elements = []

for element in range(2):
    used_elements.extend(elements[list(elements)[random.randint(0, len(elements) - 1)]].values())
    print(used_elements)
    used_elements.append(random.randint(used_elements[element][1] - 100, used_elements[element][1]))
print(used_elements)

#with open('html_test.html', 'w') as output_file:
#  r = r.text.encode('UTF-8')
#  output_file.write(str(r.text.encode('UTF-8')))

#soup = BeautifulSoup(r)
#print(soup.prettify())
#import random
#
#
#
#
#
#class material:
#    def __init__(self, temperature, specific_heat, weight, melting_temperature, evaporation_temperature, heat_of_fusion, heat_of_evaporation):
#       self.temperature = temperature
#        self.specific_heat = specific_heat
#        self.weight = weight
#        self.melting_temperature = melting_temperature
#        self.evaporation_temperature = evaporation_temperature
#        self.heat_of_fusion = heat_of_fusion
#        self.heat_of_evaporation = heat_of_evaporation
#
#    def status(self):
#        print(self.temperature)
#        print(self.specific_heat)
#        print(self.weight)
#        print(self.melting_temperature)
#        print(self.evaporation_temperature)
#        print(self.heat_of_fusion)
#        print(self.heat_of_evaporation)
#
#number_of_materials = random.randint(2, 5)
#materials = {}
#
#for element in range(number_of_materials):
#    materials[element] = material(random.randint(-100, 100), random.randint(1000, 10000), random.randint(1, 1000), random.randint(-10, 90), random.randint(-10, 90), random.randint(10000, 100000), random.randint(10000, 100000))
#
#for element in materials:
#    print(' ', element)
#    materials[element].status()