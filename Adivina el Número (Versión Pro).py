import random

class JuegoAdivinanza:

    def __init__(self):
        self.__numero_secreto = random.randint(1, 100)
        self.intentos = 0

    def jugar(self):

        print("=== ADIVINA EL NÚMERO ===")
        print("Adivina un número entre 1 y 100")

        while True:

            try:
                numero = int(input("Ingresa un número: "))
                self.intentos += 1

                if numero < self.__numero_secreto:
                    print("Muy bajo")

                elif numero > self.__numero_secreto:
                    print("Muy alto")

                else:
                    print(f"¡Ganaste en {self.intentos} intentos!")
                    self.guardar_puntaje()
                    break

            except ValueError:
                print("Error: Debes ingresar un número entero")

    def guardar_puntaje(self):

        nombre = input("Ingresa tu nombre: ")

        with open("puntajes.txt", "a") as archivo:
            archivo.write(f"{nombre} - {self.intentos} intentos\n")

        print("Puntaje guardado correctamente")


juego = JuegoAdivinanza()
juego.jugar()