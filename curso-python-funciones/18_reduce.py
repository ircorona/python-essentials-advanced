import functools

numbers = [1,2,3,4]

def accum(counter, item):
    print(counter)
    print(item)

result = functools.reduce(lambda counter, item : counter + item, numbers)

print(result)

# List of animals (ingredients)
animals = ['🐏', '🐓', '🐟', '🐖']  

# List of dishes you can make
dishes = ['🍔', '🍗', '🍣', '🥓']

# Use map to pair each animal with the dish you can make from it
result = list(map(lambda animal, dish: 'With ' + animal + ' you can make ' + dish, animals, dishes))

# Print the result
print(result)

# List of items: cow, chicken, and potato
items = ['🐄', '🐓', '🥔']

# Use filter to keep only the potato
only_potato = list(filter(lambda item: item == '🥔', items))

# Print the result
print(only_potato)

from functools import reduce

# List of   : lettuce, cow (for beef), and bread
ingredients = ['🥬', '🐄', '🍞']

# Use reduce to combine the ingredients and produce a hamburger emoji 🍔
hamburger = reduce(lambda x, y: '🍔', ingredients)

# Print the final result
print("Final Hamburger:", hamburger)

