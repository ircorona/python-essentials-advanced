import random
countries = ["Mex", "Col", "Arg", "Usa"]

population_2  = {country:random.randint(1,500)for country in countries}
print(population_2)

result= {country: population for (country, population) in population_2.items() if population > 50}
print(result)

text= 'Hola soy Irmin'
unique = {c: c.upper() for c in text if c in 'aeiou'}
print(unique)

def run():
    text = "Hola a todos, esta es una cadena de texto de prueba."
    print(text)
    unique = { c: text.count(c) for c in text if c in 'aeiou' }
    print(f"unique: {unique}")

if __name__ == '__main__':
    run()