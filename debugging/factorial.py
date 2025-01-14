#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Diminue n pour éviter la boucle infinie
    return result

if len(sys.argv) > 1:  # Vérifie si un argument est passé
    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Veuillez fournir un entier non négatif.")
        else:
            f = factorial(num)
            print(f)
    except ValueError:
        print("Veuillez fournir un entier valide.")
else:
    print("Usage: ./factorial.py <entier>")
