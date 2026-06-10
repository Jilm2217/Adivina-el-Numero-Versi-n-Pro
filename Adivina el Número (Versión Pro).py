# Importa la librería random para generar números aleatorios
import random


# Definición de la clase
# Una clase es una plantilla para crear objetos
class JuegoAdivinanza:

    # Constructor de la clase
    # Se ejecuta automáticamente cuando se crea un objeto
    def __init__(self):

        # Atributo privado
        # Los dos guiones bajos indican encapsulamiento
        # Solo debe usarse dentro de la clase
        self.__numero_secreto = random.randint(1, 100)

        # Atributo público
        # Guarda la cantidad de intentos del jugador
        self.intentos = 0

    # Método principal del juego
    def jugar(self):

        print("=== ADIVINA EL NÚMERO ===")
        print("Adivina un número entre 1 y 100")

        # Bucle infinito hasta que el jugador gane
        while True:

            try:

                # Solicita un número al usuario
                numero = int(input("Ingresa un número: "))

                # Aumenta el contador de intentos
                self.intentos += 1

                # Compara45 el número ingresado con el secreto
                if numero < self.__numero_secreto:
                    print("Muy bajo")

                elif numero > self.__numero_secreto:
                    print("Muy alto")

                else:
                    # Si adivina el número
                    print(f"¡Ganaste en {self.intentos} intentos!")

                    # Guarda el puntaje
                    self.guardar_puntaje()

                    # Termina la partida actual
                    return

            # Captura errores si el usuario escribe letras
            except ValueError:
                print("Error: Debes ingresar un número entero")

    # Método para guardar el resultado
    def guardar_puntaje(self):

        # Solicita el nombre del jugador
        nombre = input("Ingresa tu nombre: ")

        # Abre el archivo en modo append ("a")
        # Si no existe, Python lo crea
        with open("puntajes.txt", "a") as archivo:

            # Escribe el nombre y los intentos
            archivo.write(f"{nombre} - {self.intentos} intentos\n")

        print("Puntaje guardado correctamente")

        # Muestra el ranking actualizado
        self.mostrar_ranking(nombre)

        print("\nIniciando una nueva partida...\n")

        # Crea un nuevo objeto para reiniciar el juego
        nuevo_juego = JuegoAdivinanza()

        # Inicia otra partida
        nuevo_juego.jugar()

    # Método para mostrar el ranking
    def mostrar_ranking(self, nombre_jugador):

        # Lista donde se almacenarán los puntajes
        puntajes = []

        # Abre el archivo en modo lectura ("r")
        with open("puntajes.txt", "r") as archivo:

            # Lee todas las líneas del archivo
            lineas = archivo.readlines()

        # Recorre cada línea
        for linea in lineas:

            # Divide la línea en nombre e intentos
            nombre, intentos = linea.strip().split(" - ")

            # Convierte los intentos a entero
            intentos = int(intentos.split()[0])

            # Guarda la información en una tupla
            puntajes.append((nombre, intentos))

        # Ordena los puntajes de menor a mayor
        # Menos intentos = mejor posición
        puntajes.sort(key=lambda x: x[1])

        print("\n=== RANKING ===")

        # Muestra los primeros 5 lugares
        for posicion, (nombre, intentos) in enumerate(puntajes[:5], start=1):
            print(f"{posicion}. {nombre} - {intentos} intentos")

        # Variable para guardar la posición del jugador actual
        posicion_jugador = None

        # Busca la posición del jugador
        for posicion, (nombre, intentos) in enumerate(puntajes, start=1):

            if nombre == nombre_jugador and intentos == self.intentos:
                posicion_jugador = posicion
                break

        # Si quedó fuera del Top 5
        if posicion_jugador is not None and posicion_jugador > 5:
            print("...")
            print(f"{posicion_jugador}. {nombre_jugador} - {self.intentos} intentos")


# Creación del objeto
# Aquí nace el objeto juego
juego = JuegoAdivinanza()

# Llamada al método principal
juego.jugar()