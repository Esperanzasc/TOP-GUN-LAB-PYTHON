print("Bienvenido, veamos si el número que vas a ingresar en un número primo o no...")



def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

# Pide un numero al usuario
num = int(input("Ingrese el número que quiere verificar: "))

# Verifica si el número es #primo
if is_prime(num):
    print(num, " es un número primo.")
else:
    print(num, " NO es un número primo.")