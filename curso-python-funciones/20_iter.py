'''
for i in range(1,10):
    print(i)

    my_iter = iter(range(1,3))
    print(my_iter)
    print(next(my_iter))
'''


fruit = ("manzana", "pera", "banano")
myit = iter(fruit)

print(next(myit))  # Imprime: manzana
print(next(myit))  # Imprime: pera
print(next(myit))  # Imprime: banano

#for
cars = ('chevrolet', 'volvo', 'audi', 'mazda') 
for x in cars:
  print(x)

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))  # Imprime: 1
print(next(myiter))  # Imprime: 2
print(next(myiter))  # Imprime: 3

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 10:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
