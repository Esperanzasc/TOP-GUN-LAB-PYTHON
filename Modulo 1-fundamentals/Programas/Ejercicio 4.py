import re

def extraer_numeros(cadena):
    numeros_encontrados = re.findall(r'\d+', cadena)
    numeros_enteros = [int(numero) for numero in numeros_encontrados]
    return numeros_enteros

cadena = "123 todo mundo alrevez 321"
numeros = extraer_numeros(cadena)
print(numeros)