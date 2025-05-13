#!/usr/bin/python3

import sys

def fizzbuzz(n):
    """Affiche les nombres de 1 à n avec les règles FizzBuzz."""
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

# Vérifier si un argument a été fourni
if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])  # Convertir l'argument en entier
            fizzbuzz(n)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    else:
        print("Usage: ./0-fizzbuzz.py <nombre>")
