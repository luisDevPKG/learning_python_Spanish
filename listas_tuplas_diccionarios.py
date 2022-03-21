
"""
Este script contiene el uso de listas y tuplas en python.
Lo que se presenta acontinuacion hace parte del aprendizaje de cursos online que he tomado para desarrollar habilidades
en programacion, con el objetivo de crecer personal y profesionalmente

by Luis Fernando Mosquera, Ingeniero Electronico y Desarrollador Junior

"""

# LISTAS

nombres = ['Juan', 'Karla', 'Maria', 'Luis']
print(nombres)
# acceder de forma individual al elemento
print(nombres[0])
print(nombres[-1])  # de forma inversa

# cuando se trabaja con rangos:
print(nombres[0:2])  # no incluye el indice 2
# recorrer la lista desde el inicio sin incluir el indice 3
print(nombres[:3])

# desde el indice indicado hasta el final
print(nombres[1:])

# cambiar valor
nombres[0] = 'Rana rené'
print(nombres)



# ---- iterar lista -------
for nombre in nombres:
    print(nombre)
else:
    print('No existe mas contenido en la lista')

# preguntar tamaño de la lista
print(len(nombres))

# agregar elemento
nombres.append('Pinocho')
print(nombres)

# agregar elemento en un indice especifico
nombres.insert(0, 'Perez')
print(nombres)

# remover elemento
nombres.remove('Perez')
print(nombres)

# remover ultimo valor agregado
nombres.pop()
print(nombres)

# remover elemento en indice especifico
del nombres[0]
print(nombres)

# limpiar lista
nombres.clear()
print(nombres)

# eliminar lista por completo
# del nombres
# print(nombres)


# ------------------   EJERCICIO -------------------------
print('Algoritmo que te imprime sólo los números que son divisibles por 3, en un rango entre 0 y 10')
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for resultado in numeros[1:]:
    if resultado % 3 == 0:
        print(resultado)



#  *** TUPLAS ***

# definir tupla
frutas = ('Naranja', 'Guayaba', 'Mora')
print(frutas)
print(len(frutas))
# acceder a un elemento
print(frutas[0])
# navegacion inversa
print(frutas[-1])
# acceder a un rango
print(frutas[0:2])  # no incluye el ultimo indice
# recorrer elementos tuplas
for fruta in frutas:
    print(fruta, end=' ')
# cambiar valor tupla
frutaLista = list(frutas)
frutaLista[0] = 'Pera'
frutas = tuple(frutaLista)
print('\n', frutas)

# eliminar tupla
# del frutas
# print(frutas)

# ----------  EJERCICIO TUPLA Y LISTA ---------------
numTupla = (13, 1, 8, 3, 2, 5, 8)
newlist = []
for lista in numTupla:
    if lista < 5:
        newlist.append(lista)
print(newlist)


# ** SET **
planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)
# tamaño
print(len(planetas))
# revisar elemento presente o no
print('Marte' in planetas)
# agregar elemento
planetas.add('Tierra')
print(planetas)
# NO se pueden duplicar elementos
# eliminar elementos
planetas.remove('Tierra')
print(planetas)
planetas.discard('Jupiter') # elimina elemento si está, si no está no tira error, no elimina nada
# limpiar set
planetas.clear()
print(planetas)
# eliminar set
#del planetas
#print(planetas)


# *** DICCIONARIOS ***
diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
print(diccionario)
# tamaño
print(len(diccionario))
# acceder a un elemento (key)
print(diccionario['IDE'])
# otra forma de recuperar elemento
print(diccionario.get('OOP'))
# modificar elementos
diccionario['IDE'] = 'integrated development environment'
print(diccionario)
# recorrer elementos
for termino, valor in diccionario.items(): # item permite entregar los elementos separados por termino y valor
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

# comprobar existencia elemento
print('IDE' in diccionario)

# agregar elemento
diccionario['PK'] = 'Primary key'
print(diccionario)
# remover elemento
diccionario.pop('DBMS')
print(diccionario)
# limpiar diccionario
diccionario.clear()
print(diccionario)
# elminar diccionario
#del diccionario
#print(diccionario)