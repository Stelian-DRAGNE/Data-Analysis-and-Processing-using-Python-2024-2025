
lista = [10, 2, 30, 50, 300, 10]

# Versiunea 1 - filter + functie
def elimina_elemente(element):
    return element > 5
print(list(filter(elimina_elemente, lista)))

# Versiunea 2 - filter + functie lambda
print(list(filter(lambda x : x > 5, lista)))

# Versiunea 3 - list comprehention
print([element for element in lista if element > 5])