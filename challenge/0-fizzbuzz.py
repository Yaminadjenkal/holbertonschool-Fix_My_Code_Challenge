#!/usr/bin/python3

def fizzbuzz(n):
    """Affiche les nombres de 1 à n avec les règles FizzBuzz."""
    for i in range(1, n + 1):  # Assurez-vous de bien inclure `n` dans la boucle
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

# Exécuter le script avec 89
fizzbuzz(89)
