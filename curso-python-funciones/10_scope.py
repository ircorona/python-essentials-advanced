# Scope Local
# Una variable construida dentro de una función pertenece al ámbito local de esa función.
# Solo se puede usar dentro de esa función.
def incrementar():
  x = 150
  print(x)

incrementar()
# Resultado: 150

# Scope Global
# Una variable creada en la parte externa de una función y puede ser utilizada tanto de manera global como local.
y = 150
def incrementar_2():
  print(y)

print(y)
# Resultado: 150
incrementar_2()
# Resultado: 150

# Variables Globales y Locales con el Mismo Nombre
# Si tenemos dos variables, una global y la otra local con el mismo nombre,
# Python las tomará por separado, siendo una de tipo global (fuera de la función)
# y la otra de tipo local (dentro de la función).
y = 150
def incrementar_2():
  y = 300
  print(y)

incrementar_2()
print(y)
# Resultado:
# 300
# 150

# Truco: Usar `global` dentro de una Función
# Si una variable global se usa dentro de un ámbito local,
# podemos utilizar `global` para que la variable se vuelva de ámbito global dentro de la función.
def incrementar_3():
  global x
  x = 250

incrementar_3()
print(x)
# Resultado: 250

# También podemos utilizar `global` dentro de una función para reemplazar un valor de tipo local a uno global.
y = 150
def incrementar_2():
  global y
  y = 300

incrementar_2()
print(y)
# Resultado: 300
