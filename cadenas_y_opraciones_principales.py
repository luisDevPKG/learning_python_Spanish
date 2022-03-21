
"""
Este script contiene manejo de cadenas en python, operaciones matematcias principales y el uso de operadores logicos.
Lo que se presenta acontinuacion hace parte del aprendizaje de cursos online que he tomado para desarrollar habilidades
en programacion, con el objetivo de crecer personal y profesionalmente

by Luis Fernando Mosquera, Ingeniero Electronico y Desarrollador Junior

"""

# *** MANEJO DE CADEJAS ****

nombre = 'luis'
apellido = 'mosquera'
print('Mi nombre es: ' + nombre + ' ' + apellido)

print('Mi nombre es:', nombre, apellido)

numero1 = '1'
numero2 = '2'
print('Concatenacion: ' + numero1 + numero2)
print(int(numero1) + int(numero2))


# **** OPERADORES PYTHON ****
operandoA = 3
operandoB = 2
suma = operandoA + operandoB
# print('El resultado es:', suma)
print(f'El resultado de la suma es: {suma}')

# Resta
resta = operandoA - operandoB
print(f'El resultado de la resta es: {resta}')

# multiplicacion
multiplicacion = operandoA * operandoB
print(f'El resultado de la multiplicación es: {multiplicacion}')

# division
division = operandoA / operandoB
print(f'El resultado de la división es: {division}')
division = operandoA // operandoB
print(f'El resultado de la división (en numero entero) es: {division}')

# módulo
modulo = operandoA % operandoB
print(f'El resultado del módulo es: {modulo}')

# exponente
exponente = operandoA ** operandoB
print(f'El resultado de exponente es: {exponente}')


# ------------ EJERCICIO --------------------------------
print("Calcular área y perímetro de un rectángulo")
alto = int(input("Por favor ingrese la altura del rectángulo: "))
ancho = int(input("Por favor ingrese el ancho del rectángulo: "))
print(f'La altura del rectángulo es: {alto}')
print(f'El ancho del rectángulo es: {ancho}')
area = alto * ancho
perimetro = (alto + ancho) * 2
print(f'*** El área del rectángulo es: {area} ***')
print(f'*** El perímetro del rectángulo es: {perimetro} **+')

# OPERACION DE ASIGNACION Y REASIGNACION
miVariable = 10
print(miVariable)

miVariable = miVariable + 1  # reasignacion = 11
print(miVariable)

# otra equivalencia a reasignacion es
miVariable += 1
print(miVariable)

# es posible reasignar en la mayoria de operaciones: += , -= , *= , /= , **=

# OPERACION DE COMPARACION
a = 4
b = 2
resultado = (a == b)
print(f'El resultado == : {resultado}')

resultado = (a != b)
print(f'El resultado != : {resultado}')

resultado = (a > b)
print(f'El resultado > : {resultado}')
resultado = (a >= b)
print(f'El resultado >= : {resultado}')

resultado = (a < b)
print(f'El resultado < : {resultado}')
resultado = (a <= b)
print(f'El resultado <= : {resultado}')

#  -------------- EJERCICIO PAR O IMPAR ----------------------------
print("Algoritmo para determinar si el número es par o impar")
numero = int(input("Por favor ingrese un número: "))
if numero % 2 == 0:
    print(f'El número {numero} es par')
else:
    print(f'El número {numero} es impar')

#  ---------------- EJERCICIO EDAD PERSONA ------------------------
print('Algoritmo para determinar si eres o no mayor de edad')
edad = int(input('Por favor ingresa tu edad: '))
if edad >= 18:
    print(f'Felicidades tu edad es {edad}. Eres mayor de edad')
else:
    print(f'Lo siento, tu edad es {edad}. Aun eres menor de edad')

# OPERADORES LOGICOS
a = True
b = True
resultado = a and b
# print(resultado)

resultado = a or b
# print(resultado)

resultado = not a
print(resultado)

# ----------------   EJERCICIO ------------------------------
print('Algoritmo para determinar si el número está dentro del rango')
a = int(input('Por favor ingresa un número: '))
valorMin = 0
valorMax = 5
dentroRango = (a >= valorMin) and (a <= valorMax)
if dentroRango:
    print(f'Felicitaciones! el número {a} SI está dentro del rango')
else:
    print(f'Ups lo siento, pero el número {a} NO está dentro del rango')

# --------------  EJERCICIO 2 ----------------------------------
# Algoritmo para determinar si el padre puede ir a ver el juego de su hijo'
vacaciones = True
diaDescanso = False
if vacaciones or diaDescanso:
    print('Si puede asistir')
else:
    print('No puede asistir, está ocupado')

# ------------------- EJERCICIO ANTERIOR CON NOT ------------------
vacaciones = False
diaDescanso = True
if not (vacaciones or diaDescanso):
    print('No puede asistir, está ocupado')
else:
    print('Si puede asistir')

# ------------------- EJERCICIO EDAD PERSONA ---------------------
edad = int(input('Ingresa tu edad: '))
if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
    print('Estás dentro del rango de edad entre los 20\'s y los 30\'s')
else:
    print('No estás dentro del rango de edad entre los 20\'s y los 30\'s')

#  --------------------- EJERCICIO DOS NUMEROS --------------------
print('Algoritmo para determinar Qué número es MAYOR')
a = int(input('Por favor ingresa el primer número: '))
b = int(input('Por favor ingresa el segundo número: '))
if b < a > b:
    print(f'El número {a} es MAYOR que {b}')
else:
    print(f'El número {b} es Mayor que {a}')

# ----     EJERCICIO TIENDA LIBROS --------------------------------
print('Proporcinar los siguientes datos del libro:')
primerDato = input('Escribe el nombre del libro: ')
segundoDato = int(input('Escribe el ID del libro: '))
tercerDato = float(input('Escribe el precio del libro: '))
cuartoDato = input('Indica si el envío es gratuito (True/False): ')

if cuartoDato == 'True':
    cuartoDato = True
elif cuartoDato == 'False':
    cuartoDato = False
else:
    cuartoDato = 'Valor incorrecto, escribe True o False'

print(f'''
    Nombre: {primerDato}
    ID: {segundoDato}
    Precio: {tercerDato}
    Envío gratuito?: {cuartoDato}
''')