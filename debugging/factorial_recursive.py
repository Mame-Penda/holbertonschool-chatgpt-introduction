#!/usr/bin/python3
import sys

def factorial(n):
    """Calculate the factorial of a non-negative integer."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    try:
        # Vérifier qu'un argument a été fourni
        if len(sys.argv) != 2:
            print("Usage: ./factorial.py <non-negative integer>")
            return

        # Vérifier que l'argument est un entier valide
        n = int(sys.argv[1])
        if n < 0:
            print("Error: Please enter a non-negative integer.")
            return

        # Calculer et afficher la factorielle
        f = factorial(n)
        print(f"The factorial of {n} is {f}")

    except ValueError:
        print("Error: Please provide a valid integer.")

if __name__ == "__main__":
    main()
