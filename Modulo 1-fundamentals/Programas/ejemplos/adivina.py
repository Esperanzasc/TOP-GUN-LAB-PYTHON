from random import randint
from enum import Enum
from datetime import datetime

#creamos clase del nivel de dificultad

class Dificultad(Enum):
    FACIL = 1
    MEDIO = 2
    DIFICIL = 3

#Creamos la clase para el juego

class AdivinaNumero:
    def __init__(self, dificultad: Dificultad)-> None:
        self.dificultad = dificultad
        
        # creamos el número al azar

        if self.dificultad == Dificultad.FACIL:
            self.numero_adivinar = randint(1,10)
        if self.dificultad == Dificultad.MEDIO:
            self.numero_adivinar = randint(1,20)
        if self.dificultad == Dificultad.DIFICIL:
            self.numero_adivinar = randint(1,30)
    
    # Creamos la función que ejecutará el código

    def play(self):
        username = input("¡Ingrese su Usuario!: ")
        print(f"¡Bienvenido al Juego {username}!")
        print("----------------------")
        print("Trata de Adivinar El Numero Que Estoy Pensando")

        intentos = 0

        #flag

        ganar = False

        while not ganar:
            intento = int(input("Ingrese un número: "))
            intentos += 1

            if intento == self.numero_adivinar:
                print(f"¡Felicidades Ganaste con {intentos} intentos !")
                ganar = True
            elif intento < self.numero_adivinar:
                print("¡ El Numero Ingresado Es Muy Bajo!, :( ¡intenta nuevamente!")
            else: 
                print("¡ El Numero Ingresado Es Muy Alto!, :( ¡intenta nuevamente!")

    # Guardamos esto en algún lugar

        with open("puntuaciones.txt", "a") as file:

            #Obtenemos Fecha
            fecha_actual = datetime.now()
            fecha_formateada = fecha_actual.strftime("%Y-%m-%d")  # Formato: AAAA-MM-DD
            hora_formateada = fecha_actual.strftime("%H:%M:%S")  # Formato: HH:MM:SS
            
            #guardamos la info
            info = fecha_formateada + " " + hora_formateada + "," + str(intentos) + ","+ str(self.dificultad) + "," + username + "\n"
            
            file.write(info)



    

# Creamos Función para que el Usuario Elija la dificultad

def elegir_dificultad():
    modo = input("Elija La Dificultad: FACIL, MEDIO o DIFICIL: ").lower()

    if modo == "facil":
        juego = AdivinaNumero(Dificultad.FACIL)
        print("Nivel Facil Seleccionado")
    elif modo == "medio":
        juego = AdivinaNumero(Dificultad.MEDIO)
        print("Nivel Medio Seleccionado")
    elif modo == "dificil":
        juego = AdivinaNumero(Dificultad.DIFICIL)
        print("Nivel Dificil Seleccionado")
    else:
        juego = AdivinaNumero(Dificultad.MEDIO)
        print("Por Defecto Jugaras En Nivel Medio")
    
    #empezamos a jugar 

    juego.play()
#Menu del juego

def menu():
    active = True
    while active:
        print("<-----------Bienvenido al Menú del Juego----------->")
        print("1. Jugar")
        print("2. Ver Puntuación")
        print("3. Salir del juego")
        print("4. Créditos")
        
        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            elegir_dificultad()
        elif opcion == 2:
            ver_puntuacion()
        elif opcion == 3:
            print("Saliendo del Juego, hasta luego")
            active = False
        elif opcion == 4:
            creditos()
        else:
            print("Opción no Valida")


#Función para ver puntuación

def ver_puntuacion():
    try:
        with open("puntuaciones.txt", "r") as file:
            contenido = file.read()
            print("-------------------------------------")
            print(contenido)
            print("-------------------------------------")
    except FileNotFoundError:
        print("El Archivo no existe")

# creditos autor
def creditos():
    print("-------------------------------------")
    print("Creado por Mateo Soto Arango, estudiante de Matemáticas, Universidad de Antioquia")
    print("Top GunLab, 2023")
    print("Team International")
    print("-------------------------------------")



if __name__ == "__main__":
    menu()
    
        



        

    
        

    