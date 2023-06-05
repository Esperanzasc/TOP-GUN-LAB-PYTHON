import random
from enum import Enum


class Dificultad(Enum):
    FACIL = 1
    MEDIO = 2
    DIFICIL = 3


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
        number = random.randint(1, 10)
        trials = 0

        # flag variable
        win = False

        while not win:
            guess = int(input("Please enter your guess: "))
            trials += 1

            if guess == number:
                win = True
            elif guess < number:
                print("Too low")
            else:
                print("Too high")
        
        # file = open("scores.txt", "w")
        # file.write(f"Score: {trials}")
        # file.close()
        with open("scores.txt", "w") as file:
            file.write(f"Score: {trials}")

        print(f"You win with {trials} trials")


def main():
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


if __name__ == '__main__':
    main()


# TODO:
# 1. Agregar mas informacion del usuario: Nombre
# 2. Al guardar los puntajes, se guarde con el nombre de usuario y la dificultad
# 3. Al iniciar el juego mostrar un menu con 3 optiones
    # Jugar -> Al usuario elejir este menu, se debe preguntar por una dificultad
    # Mostrar puntajes
    # Creditos
    # Salir
