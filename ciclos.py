"""
Este script contiene el uso del If, For y ciclo While en python.
Lo que se presenta acontinuacion hace parte del aprendizaje de cursos online que he tomado para desarrollar habilidades
en programacion, con el objetivo de crecer personal y profesionalmente

by Luis Fernando Mosquera, Ingeniero Electronico y Desarrollador Junior

"""

# **** Uso del  IF ******

# CONVERSION NUMERO A TEXTO
numero = int(input('Digita un valor entre 1 y 3: '))
numeroTexto = ''

if numero == 1:
    numeroTexto = 'Número uno'
elif numero == 2:
    numeroTexto = 'Número dos'
elif numero == 3:
    numeroTexto = 'Número tres'
else:
    numeroTexto = 'Valor fuera de rango'

print(f'El número digitado es: {numero} --> {numeroTexto}')

# SENTENCIA IF SIMPLIFICADA (operador ternario)
condicion = True

# if condicion:
#     print('Condicion Verdadera')
# else:
#     print('Condicion Falsa')

print('Condicion verdadera') if condicion else print('Condicion Falsa')

# --------------- EJERCICIO ESTACIONES DEL AÑO --------------------
mes = int(input('Ingresa el mes del año (1 - 12): '))
estacion = None  # no continene ningun valor

if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Mes incorrecto'

print(f'Para el mes {mes} la estación es: {estacion}')

# ---------------- EJERCICIO ETAPAS SEGUN EDAD --------------------------
print('Algoritmo para indicarte la etapa de tu vida segun tu edad')
edad = int(input('Por favor ingresa tu edad: '))
etapa = None

if 0 <= edad < 10:
    etapa = '¡¡ infancia, es Increible !!'
elif 10 <= edad < 20:
    etapa = 'muchos cambios y demasiado estudio :('
elif 20 <= edad < 50:
    etapa = 'Amor y mucho trabajo'
elif 50 <= edad < 90:
    etapa = 'Jubilación, compartir en familia y envejecer'
elif 90 <= edad <= 100:
    etapa = 'Descanso eterno'
else:
    etapa = '** ERROR ** Edad fuera del rango, etapa de la vida no reconocida'
print(f'Para tu edad de {edad} estás en la etapa de {etapa} ')

# ------          EJERCICIO SISTEMA DE CALIFICACIONES ----------------------
print('Sitema de calificaciones')
calificacion = int(input('Ingresa el número de respuestas correctas (0 -10) que tuviste en el exámen: '))
resultado = None

if 0 <= calificacion < 6:
    resultado = 'Tu calificación es una F'
elif 6 <= calificacion < 7:
    resultado = 'Tu calificación es una D'
elif 7 <= calificacion < 8:
    resultado = 'Tu calificacion es una C'
elif 8 <= calificacion < 9:
    resultado = 'Tu calificacíon es una B'
elif 9 <= calificacion <= 10:
    resultado = 'Tu calificación es una A'
else:
    resultado = '** ERROR ** calificación no reconocida, respuestas correctas fuera del rango'
print(f'De acuerdo a tus respuestas correctas {calificacion}: {resultado}')




# **** Uso del FOR *****
cadena = 'Hola'
for letra in cadena:
    print(letra)
else:
    print('Fin del ciclo for')

# break en los ciclos
for palabra in 'Holanda':
    if palabra == 'a':
        print(f'Letra encontrada: {palabra}')
        break  # rompe el ciclo for
    else:
        print('Fin ciclo for')

# palabra CONTINUE
# for a in range(6):
#     if a % 2 == 0:
#         print(f'Valor: {a}')
for a in range(6):
    if a % 2 != 0:
        continue
    print(f'Valor: {a}')



# *** Uso del WHILE ****
contador = 0
while contador < 3:
    print(contador)
    contador += 1  # contador incrementando en 1
else:
    print('Fin del ciclo while')

# ---------------- EJERCICIO NUMEROS NATURALES ---------------
numero = 0
while numero <= 10:
    print(numero)
    numero += 1
else:
    print('Fin del ciclo while')

# ---------- EJERCICIO NUMEROS DE 5 A 1 ------------
i = 5
while i >= 1:
    print(i)
    i = i - 1


# ----- EJERCICIO ----
n = 5
list_number = []
while 1 <= n <= 20:
    for i in range(n):
        i = i**2
        list_number.append(i)
        print(i)
    break
else:
    print('Number out of range')