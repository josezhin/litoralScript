#!/usr/bin/python3

import argparse

#ejecutar el script en consola seguido del numero, ejemplo: python3 fibonacci.py 10

# Crear el objeto ArgumentParser y definir el argumento
parser = argparse.ArgumentParser()
parser.add_argument('numero', type=int, help='El número de términos de la sucesión de Fibonacci a calcular')

# Parsear los argumentos
args = parser.parse_args()

# Definir la función para calcular los números de Fibonacci
def fibo(x):
    a = 0
    b = 1
    for i in range(x):
        c = a + b
        a = b
        b = c
    return b ** 3

# Calcular los números de Fibonacci y mostrarlos en pantalla
for j in range(args.numero):
    print(fibo(j))
