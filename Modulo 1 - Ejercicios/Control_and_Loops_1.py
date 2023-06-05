def secuencia_fib(n):

    fib_secuencia = [0, 1]  # Inicializando la secuencia con los primeros dos numeros
    
    for i in range(2, n):
        fib_secuencia.append(fib_secuencia[i-1] + fib_secuencia[i-2])  # Agregando el proximo numero Fib
    
    return fib_secuencia


# Imprimiendo los 10 primeros numeros Fib
num_fib = secuencia_fib(10)
print("Los siguientes números son los 10 primeros números de la secuencia Fibonacci: ")
for number in num_fib:
    print(number)
