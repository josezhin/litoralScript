#!/usr/bin/python3
import requests, sys, argparse

arg = argparse.ArgumentParser()
arg.add_argument('-n', '--numero', nargs="+", type=int, help="Proporcionar una lista de números")
arg.add_argument('-d', '--divisor', nargs=1, type=int, help="proporcionar un número divisor")

argumento = arg.parse_args()
numeros = argumento.numero

if argumento.divisor != None:
    divisor = argumento.divisor[0]
    divisible = False
    for numero in numeros:
        if divisor % numero == 0:
            divisible = True
            break
    if argumento.numero != None:
        if divisible:
            print(f"\n Hay un numero que es divisible por {divisor}")
        else:
            print(f"\n Ningun numero es divisible por {divisor}")
else:
    print("\n Uso: python3 " + sys.argv[0]+ " -n <Lista de números> " + "-d <Numero divisor>")
