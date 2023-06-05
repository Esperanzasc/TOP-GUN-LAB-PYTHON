def reverse_string(string):
    return string[::-1]     #El operador [::-1] indica que se tomen los elementos desde el final hasta el principio, tomando cada uno en orden inverso.


texto = input("Ingrese un texto para invertir: ")
text_invert = reverse_string(texto)

print("Su texto ingresado fue: ", texto)
print("El texto invertido es: ", text_invert)

