"""Comparación experimental entre insertion sort y merge sort."""

import os
import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3


def medir(algoritmo, datos: list[int]) -> float:
    """Mide el tiempo promedio de un algoritmo.

    Args:
        algoritmo: Función de ordenamiento.
        datos: Lista de datos que se va a ordenar.

    Returns:
        Tiempo promedio en segundos.
    """
    tiempos = []

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        algoritmo(datos)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)

    return sum(tiempos) / REPETICIONES


def ejecutar_comparacion() -> None:
    """Mide los dos algoritmos y genera la gráfica."""
    tiempos_insertion = []
    tiempos_merge = []

    print("Resultados Parte 4")

    for n in TAMANOS:
        datos = generar_aleatorio(n)

        tiempo_insertion = medir(insertion_sort, datos)
        tiempo_merge = medir(merge_sort, datos)

        tiempos_insertion.append(tiempo_insertion)
        tiempos_merge.append(tiempo_merge)

        print(
            f"n={n:5d} | insertion={tiempo_insertion:.8f}s | "
            f"merge={tiempo_merge:.8f}s"
        )

    os.makedirs("graficas", exist_ok=True)

    plt.plot(
        TAMANOS,
        tiempos_insertion,
        marker="o",
        label="Insertion sort",
    )
    plt.plot(
        TAMANOS,
        tiempos_merge,
        marker="o",
        label="Merge sort",
    )

    plt.title("Comparación de tiempos de ordenamiento")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/parte4_tiempo.png")
    plt.close()


if __name__ == "__main__":
    ejecutar_comparacion()