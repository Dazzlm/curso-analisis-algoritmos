"""Subarreglo maximo: fuerza bruta y divide y venceras."""


def subarreglo_fuerza_bruta(
    valores: list[float],
) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de dias.

    Args:
        valores: variacion diaria de caja, una por dia. Tiene al menos
            un elemento.

    Returns:
        Una tupla (inicio, fin, suma) con los indices inclusivos del
        tramo de mayor suma y el valor de esa suma.
    """
    mejor_inicio = 0
    mejor_fin = 0
    mejor_suma = valores[0]

    for inicio in range(len(valores)):
        suma_actual = 0

        for fin in range(inicio, len(valores)):
            suma_actual += valores[fin]

            if suma_actual > mejor_suma:
                mejor_suma = suma_actual
                mejor_inicio = inicio
                mejor_fin = fin

    return mejor_inicio, mejor_fin, mejor_suma


def suma_cruzada(
    valores: list[float],
    inicio: int,
    medio: int,
    fin: int,
) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango considerado.
        medio: indice del ultimo elemento de la mitad izquierda.
        fin: indice final del rango considerado.

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye
        elementos de ambas mitades.
    """
    suma_actual = 0
    mejor_izquierda = float("-inf")
    indice_izquierda = medio

    for i in range(medio, inicio - 1, -1):
        suma_actual += valores[i]

        if suma_actual > mejor_izquierda:
            mejor_izquierda = suma_actual
            indice_izquierda = i

    suma_actual = 0
    mejor_derecha = float("-inf")
    indice_derecha = medio + 1

    for j in range(medio + 1, fin + 1):
        suma_actual += valores[j]

        if suma_actual > mejor_derecha:
            mejor_derecha = suma_actual
            indice_derecha = j

    return (
        indice_izquierda,
        indice_derecha,
        mejor_izquierda + mejor_derecha,
    )


def subarreglo_maximo(
    valores: list[float],
    inicio: int,
    fin: int,
) -> tuple[int, int, float]:
    """Encuentra la mejor racha por divide y venceras.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango a considerar.
        fin: indice final del rango a considerar.

    Returns:
        Una tupla (inicio, fin, suma) del tramo de mayor suma.
    """
    if inicio == fin:
        return inicio, fin, valores[inicio]

    medio = (inicio + fin) // 2

    izquierda = subarreglo_maximo(valores, inicio, medio)
    derecha = subarreglo_maximo(valores, medio + 1, fin)
    cruzada = suma_cruzada(valores, inicio, medio, fin)

    mejor = izquierda

    if derecha[2] > mejor[2]:
        mejor = derecha

    if cruzada[2] > mejor[2]:
        mejor = cruzada

    return mejor