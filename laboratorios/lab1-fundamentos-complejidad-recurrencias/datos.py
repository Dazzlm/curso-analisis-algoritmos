"""Generadores de lotes de registros para los escenarios de Tamiza."""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera datos aleatorios para el escenario A.

    Args:
        n: Cantidad de registros.
        semilla: Valor para repetir el experimento.

    Returns:
        Lista de índices de riesgo desordenados.
    """
    generador = random.Random(semilla)
    datos = list(range(1, n + 1))
    generador.shuffle(datos)
    return datos


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera datos casi ordenados para el escenario B.

    El 98 % está ordenado y el 2 % restante se coloca al final.

    Args:
        n: Cantidad de registros.
        semilla: Valor para repetir el experimento.

    Returns:
        Lista casi ordenada de mayor a menor.
    """
    generador = random.Random(semilla)

    cantidad_ordenada = int(n * 0.98)
    cantidad_nueva = n - cantidad_ordenada

    datos = list(range(n, cantidad_nueva, -1))
    nuevos = list(range(cantidad_nueva, 0, -1))

    generador.shuffle(nuevos)

    return datos + nuevos


def generar_inverso(n: int) -> list[int]:
    """Genera datos en orden inverso para el escenario C.

    Args:
        n: Cantidad de registros.

    Returns:
        Lista ordenada de menor a mayor.
    """
    return list(range(1, n + 1))