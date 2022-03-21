
"""
Este script contiene el uso de Funciones en python.
Lo que se presenta acontinuacion hace parte del aprendizaje de cursos online que he tomado para desarrollar habilidades
en programacion, con el objetivo de crecer personal y profesionalmente

by Luis Fernando Mosquera, Ingeniero Electronico y Desarrollador Junior

"""

# FUNCIONES
def mi_funcion(nombre, apellido):
    print('Saludos desde mi función')
    print(f'Hola {nombre} {apellido}')


mi_funcion('Luis', 'Mosquera')


# ejercicio ejemplo
def sumar(a, b):
    return a + b


resultado = sumar(1, 2)
print(f'El resultado de la suma es: {resultado}')
# print(f'El resultado de la suma es: {sumar(5, 3)}')

# valores por default, sin embargo se puede sobreescribir ingresando otros argumentos en la funcion
# def sumar(a = 0,b = 0):
#   return a+b
#
# resultado = sumar(1, 2)
# print(f'El resultado de la suma es: {resultado}')


# def sumar(a:int = 0, b:int = 0) -> int:
# indica que tipo de dato puede regresar pero no es obligatorio que sea ese mismo tipo
# sin embargo puede ser redundante
#   return a+b
#
# resultado = sumar(1, 2)
# print(f'El resultado de la suma es: {resultado}')



# *** ARGUMENTOS VARIABLES EN FUNCIONES ***
def listarNombres(*nombres):   # el * indica que se recibe una cantidad de argumentos variable
    for nombre in nombres:
        print(nombre)

listarNombres('Rana', 'raton', 'pinocho')
listarNombres('maria', 'luis')

# -----    EJERCICIO funcion que retorna la suma te los argumentos dados --------
def my_function(*num):
    resultado = 0
    for x in num:
        resultado += x
    return resultado
print(my_function(1,2,3))

# ----- EJERCICIO funcion que retorna la multiplicación te los argumentos dados --------
def my_other_function(*number):
    resp = 1
    for y in number:
        resp *= y
    return resp
print(my_other_function(5,2,3))


# Tema funciones llave - valor (kywargs)
def listaTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor:}')
listaTerminos(IDE='Integrated Development Environment', PK = 'Primary Key')

# distintos tipos de dato como argumento
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres = ['Lucho', 'Maria']
desplegarNombres(nombres)
desplegarNombres('Roca')
# desplegarNombres(10) y desplegarNombres(10, 11) da error porque no es posible
desplegarNombres((10, 11)) # funciona porque (10, 11) representa una tupla
desplegarNombres([10, 11])

# ** FUNCIONES RECURSIVAS ** # mandar a llamar a una funcion asi misma
print('Conoce el factorial de cualquier número!')
numero = int(input('Ingresa el número: '))
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)
resultado = factorial(numero)
print(f'El factorial de {numero} es: {resultado}')


# -----  EJERCICIO Imprimir numeros de 5 a 1 de manera descendente implementando funciones recursivas ---------
def numb_descendente(numb):
    if numb < 0:
        return
    elif 0 <= numb <= 5:
        print(numb)
        numb_descendente(numb-1)
numb_descendente(5)

# --------------- EJERCICIO  Calculadora de impuestos ----------------
print('Calcula el pago con el impuesto')
pago_sin_impuesto = float(input('Ingresa el valor a pagar: '))
impuesto = float(input('Ingresa el valor del impuesto (%): '))
def calcular_total(pago_sin_impuesto, impuesto):
    conversion = impuesto/100
    return pago_sin_impuesto + (pago_sin_impuesto * conversion)
pagar = calcular_total(pago_sin_impuesto, impuesto)
print(f'El total a pagar es de : {pagar}')


# ------------------ EJERCICIO CONVERSIÓN DE TEMPERATURA celsius a fahrenheit ----------------
print('Algoritmo para la conversión de temperatura:')
print('** Convertir de grados Celsius a Fahrenheit **')
gradoCelsius = float(input('Ingresa la temperatura en grados Celsius: '))
def celsius_fahrenheit(gradoCelsius):
    return (gradoCelsius * (9/5)) +32
result1 = celsius_fahrenheit(gradoCelsius)
resul_corto1 = round(result1,5)
# print(f'Los grados ({gradoCelsius}°C) equivalen a {result1} grados Fahrenheit (°F)')
print(f'Los grados ({gradoCelsius}°C) equivalen a {resul_corto1} grados Fahrenheit (°F)')

#  ---------------- EJERCICIO CONVERSIÓN DE TEMPERATURA fahrenheit a celsius ----------------
print('Algoritmo para la conversión de temperatura:')
print('** Convertir de grados Fahrenheit a Celsius **')
gradoFahrenheit = float(input('Ingresa la temperatura en grados Fahrenheit: '))
def celsius_fahrenheit(gradoFahrenheit):
    return (gradoFahrenheit - 32) * (5/9)
result2 = celsius_fahrenheit(gradoFahrenheit)
resul_corto2 = round(result2,5)
# print(f'Los grados ({gradoFahrenheit}°F) equivalen a {result2} grados Celsius (°C)')
print(f'Los grados ({gradoFahrenheit}°F) equivalen a {resul_corto2} grados Celsius (°C)')