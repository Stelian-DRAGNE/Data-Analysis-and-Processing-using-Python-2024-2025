from django.test import TestCase

# Create your tests here.

def factorial(n):
    if n == 0 or n ==1:
        return 1
        
    return n * factorial(n - 1)

# print(factorial(7))

n = 8
lista_factorial = []
for i in range(n, -1, -1):
    lista_factorial.append((i, factorial(i)))
print(lista_factorial)