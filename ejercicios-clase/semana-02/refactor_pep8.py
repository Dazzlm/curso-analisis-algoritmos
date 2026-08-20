def calcular_promedio(lista_numeros: list[int]) -> float:
    """Calcula el promedio de una lista de números.

    Args:
        lista_numeros: Lista de números enteros.

    Returns:
        El promedio de los números.
    """
    suma = 0

    for numero in lista_numeros:
        suma += numero

    return suma / len(lista_numeros)


def main() -> None:
    """Ejecuta el programa principal."""
    numeros = [1, 2, 3, 4, 5]
    promedio = calcular_promedio(numeros)
    print(promedio)


if __name__ == "__main__":
    main()