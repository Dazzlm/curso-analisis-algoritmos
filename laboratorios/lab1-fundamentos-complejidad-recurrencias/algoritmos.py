"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de mayor a menor usando inserción.

    No modifica la lista original.

    Args:
        datos: Lista de índices de riesgo.

    Returns:
        Una tupla con la lista ordenada y el número de comparaciones.
    """
    lista = datos.copy()
    comparaciones = 0

    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1

        while j >= 0:
            comparaciones += 1

            if lista[j] >= actual:
                break

            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = actual

    return lista, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de mayor a menor usando merge sort.

    No modifica la lista original.

    Args:
        datos: Lista de índices de riesgo.

    Returns:
        Una tupla con la lista ordenada y el número de comparaciones.
    """
    if len(datos) <= 1:
        return datos.copy(), 0

    mitad = len(datos) // 2
    izquierda, comparaciones_izq = merge_sort(datos[:mitad])
    derecha, comparaciones_der = merge_sort(datos[mitad:])

    resultado = []
    i = 0
    j = 0
    comparaciones = comparaciones_izq + comparaciones_der

    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1

        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado, comparaciones