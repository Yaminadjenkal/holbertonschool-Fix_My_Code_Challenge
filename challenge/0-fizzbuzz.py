#!/usr/bin/python3

def fizzbuzz(n):
    """Affiche les nombres de 1 à n en remplaçant les multiples de 3 et 5."""
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

# Appel de la fonction avec 50
fizzbuzz(89)
