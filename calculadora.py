def sumar(cadena: str) -> int:
    if cadena == "":
        return 0

    numeros = cadena.split(",")
    return sum(int(numero) for numero in numeros)
