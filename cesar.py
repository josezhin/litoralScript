#!/usr/bin/python3

import argparse


#ejecutar el script en la consola, ejemplo: python3 cesar.py Lspe 4

# Crear el objeto ArgumentParser y definir los argumentos
parser = argparse.ArgumentParser(description='Cifrado César')
parser.add_argument('mensaje_codificado', type=str, help='El mensaje codificado a descifrar')
parser.add_argument('clave', type=int, help='La clave para descifrar el mensaje')

# Parsear los argumentos
args = parser.parse_args()

# Descifrar el mensaje
m_descifrado = ""
for alfabeto in args.mensaje_codificado:
    if alfabeto.isalpha():
        n = ord(alfabeto)
        n -= args.clave
        if alfabeto.isupper():
            if n < ord('A'):
                n += 26
        else:
            if n < ord('a'):
                n += 26
        alfabeto_descifrado = chr(n)
        m_descifrado += alfabeto_descifrado
    else:
        m_descifrado += alfabeto

print("El mensaje decifrado es:", m_descifrado)
