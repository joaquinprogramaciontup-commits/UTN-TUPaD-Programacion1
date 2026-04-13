import math
#Ejercisio 1
print("Hola Mundo!")
#Ejercisio 2
nombre = input("Ingrese su nombre para ser saludado: ")
print(f'Hola {nombre}!')
#Ejercisio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
ubicacion = input("Ingrese su ciudad de residencia: ")
print(f'Soy {nombre} {apellido}, tengo {edad} y vivo en {ubicacion}')
#Ejercisio 4
radio = int(input("Ingrese el radio de un circulo para calcular su area y perimetro: "))
area = radio * (math.pi **2)
perimetro = 2 * math.pi * radio
print(f'El area del circulo es {area} y su perimetro es {perimetro}')
#Ejercisio 5
segundos = float(input("Ingrese una cantidad de segundos para calcular a cuantas horas equivale: "))
print(f'{segundos} equivale a {(segundos/60)/60} horas')
#Ejercisio 6
numero = int(input("Ingrese un numero para conocer su tabla de multiplicar: "))
print(f'{numero}\n{numero*2}\n{numero*3}\n{numero*4}\n{numero*5}\n{numero*6}\n{numero*7}\n{numero*8}\n{numero*9}\n{numero*10}\n ')
#Ejercisio 7
numero1 = int(input("Ingrese un numero entero distinto de cero: "))
numero2 = int(input("Ingrese otro numero entero distinto de cero: "))
print(f'La suma de estos numeros es: {numero1+numero2}\nLa resta de estos numeros es: {numero1-numero2}\nLa division de estos numeros es: {numero1/numero2}\nLa multiplicacion de estos numeros es: {numero1*numero2}\n')
#Ejercisio 8
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
print(f'Su indice de masa corporal es: {peso/(altura**2)}')
#Ejercisio 9
celcius = float(input("Ingrese una temperatura celcius para convertirla a Farenheit: "))
print(f'La temperatura en Farenheit es {9/5*celcius+32}')
#Ejercisio 10
numero1 = float(input("Ingrese un numero: "))
numero2 = float(input("Ingrese un numero: "))
numero3 = float(input("Ingrese un numero: "))
print(f'El promedio de estos tres numeros es {(numero1+numero2+numero3)/3}')