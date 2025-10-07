#CREA UN ISOGRAMA ES DECIR UN STRING EN DONDE NO EXISTEN LETRAS REPETIDAS
import os #os es un módulo built-in de Python que proporciona funciones para interactuar con el sistema operativo.

def es_isograma(palabra):
    return len(palabra) == len(set(palabra.lower()))

while True:
    os.system('cls' if os.name == 'nt' else 'clear')#específicamente para limpiar la pantalla 
    #os.system() - Ejecuta comandos del sistema operativo
    # #os.name - Detecta el tipo de sistema ('nt' = Windows, 'posix' = Unix/Linux/Mac)
    # #'cls' - Comando de Windows para limpiar consola
    # #'clear' - Comando de Unix/Linux/Mac para limpiar consola
    palabra = input("Escribe una palabra (o 'q' para salir): ")
    if palabra.lower() == 'q':
        break
    print(f"'{palabra}' {'ES' if es_isograma(palabra) else 'NO es'} un isograma")
    input("\nPresiona Enter para continuar...")