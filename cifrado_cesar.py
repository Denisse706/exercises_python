#encriptar frase estilo cesar, en donde las letras sustitidas sean el número de letras que se elija
def cesar_encriptar(frase: str, desplazamiento: int) -> str:
    resultado = ""

    for caracter in frase:
        if caracter.isalpha(): 
            base = ord('A') if caracter.isupper() else ord('a')
            nueva_pos = (ord(caracter) - base + desplazamiento) % 26
            nuevo_caracter = chr(base + nueva_pos)
            resultado += nuevo_caracter
        else:
            resultado += caracter  

    return resultado


def main():
    try:
        desplazamiento = int(input("Ingrese el número de saltos de letras que desea: "))
        frase = input("Ingrese la frase a encriptar: ")
        frase_encriptada = cesar_encriptar(frase, desplazamiento)
        print("Frase encriptada:", frase_encriptada)
    except ValueError:
        print("Por favor, ingrese un número válido.")


if __name__ == "__main__":
    main()