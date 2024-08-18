dictionary = {}
for i in range (1,5):
    dictionary[i] = i *2
print(dictionary)

dictionary_2 = {i: i * 2 for i in range (1,5)}
print(dictionary_2)

import random
countries = ["Mex", "Col", "Arg", "Usa"]
population = {}
for country in countries:
    population[country] = random.randint(1,500)

print(population)

population_2  = {country:random.randint(1,500)for country in countries}
print(population_2)

names = ["Irmin", "Sally", "Danbi"]
ages = [34,27,31]
print(list(zip(names,ages)))

new_dictionary = {name:age for (name, age) in zip(names, ages)}
print(new_dictionary)

#aporte de companero 
names = ['nico', 'zule', "santi"]
edades = [12,56,98]
new_dict = {names[i]:edades[i] for i in range(len(names))}
print(new_dict)