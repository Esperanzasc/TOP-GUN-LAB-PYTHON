import random
from enum import Enum
import json
from datetime import datetime


class Dificultad(Enum):
    FACIL = 1
    MEDIO = 2
    DIFICIL = 3


def get_input(prompt, options, _type):
    while True:
        user_input = input(prompt)

        if _type(user_input) in options:
            return _type(user_input)
        else:
            print("Entrada incorrecta!!!")


def show_scores():
    with open("scores.json", "r") as file:
        scores = json.load(file)
    
    print("nombre - intentos - dificultad")
    for score in scores:
        print(f"{score['username']} - {score['trials']} - {score['dificultad']}")


class GuestYourNumber:
    def __init__(self, dificultad: Dificultad) -> None:
        self.dificultad = dificultad

        if self.dificultad == Dificultad.FACIL:
            self.number = random.randint(1, 10)

        if self.dificultad == Dificultad.MEDIO:
            self.number = random.randint(1, 20)

        if self.dificultad == Dificultad.DIFICIL:
            self.number = random.randint(1, 30)
    
    def run(self):
        trials = 0

        # flag variable
        win = False

        while not win:
            guess = self.get_input(prompt="Please enter your guess: ", options=range(1, 30), _type=int)
            trials += 1

            if guess == self.number:
                win = True
            elif guess < self.number:
                print("Too low")
            else:
                print("Too high")
            
        username = input("Ingrese su nombre: ")
        print(f"{username} has ganado con {trials} intentos")

        with open("scores.json", "r") as file:
            scores = json.load(file)

        scores.append({
            "username": username,
            "dificultad": str(self.dificultad),
            "trials": trials,
            "fecha": datetime.now()
        })

        with open("scores.json", "w") as file:
            json.dump(scores, file)

# JSON: Notacion de objetos en javascription

def main():
    print("Bienvenido a Guest Your Number")

    while True:
        print("1. Jugar")
        print("2. mostrar puntajes")
        print("3. Creditos")
        print("4. Salir")

        user_input = get_input("Elije una opcion> ", [1, 2, 3, 4], int)

        if user_input == 1:
            dificultad_map = {
                "facil": Dificultad.FACIL,
                "medio": Dificultad.MEDIO,
                "dificil": Dificultad.DIFICIL
            }

            print("Elija la dificultad: ")
            print("1. facil")
            print("2. medio")
            print("3. dificil")
            user_input = input("> ")

            dificultad = dificultad_map.get(user_input, Dificultad.MEDIO)
            game = GuestYourNumber(dificultad)
            game.run()
        elif user_input == 2:
            show_scores()
        elif user_input == 3:
            print("Luis Papiernik")
        else:
            pass


if __name__ == '__main__':
    main()


# TODO:
# 1. Agregar mas informacion del usuario: Nombre
# 2. Al guardar los puntajes, se guarde con el nombre de usuario y la dificultad
# 3. Al iniciar el juego mostrar un menu con 3 optiones
    # Jugar -> Al usuario elejir este menu, se debe preguntar por una dificultad
    # Mostrar puntajes
    # Creditos -> Tu nombre, Casa software
    # Salir
