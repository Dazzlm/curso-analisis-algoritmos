"""Experimento de insertion sort con los tres escenarios de Tamiza."""

import os
import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3


def medir_tiempo(datos: list[int]) -> tuple[float, int]:
    """Mide el tiempo de insertion sort.

    Args:
        datos: Lista de datos que se va a ordenar.

    Returns:
        Tiempo promedio y comparaciones realizadas.
    """
    tiempos = []
    comparaciones = 0

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(datos)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)

    return sum(tiempos) / REPETICIONES, comparaciones


def ejecutar_experimento() -> None:
    """Ejecuta las mediciones y genera las gráficas."""
    escenarios = {
        "Aleatorio": generar_aleatorio,
        "Casi ordenado": generar_casi_ordenado,
        "Inverso": generar_inverso,
    }

    resultados = {
        nombre: {"tiempos": [], "comparaciones": []}
        for nombre in escenarios
    }

    for nombre, generador in escenarios.items():
        print(nombre)

        for n in TAMANOS:
            datos = generador(n)
            tiempo, comparaciones = medir_tiempo(datos)

            resultados[nombre]["tiempos"].append(tiempo)
            resultados[nombre]["comparaciones"].append(comparaciones)

            print(
                f"n={n:5d} | tiempo={tiempo:.8f}s | "
                f"comparaciones={comparaciones}"
            )

    os.makedirs("graficas", exist_ok=True)

    for nombre, resultado in resultados.items():
        plt.plot(
            TAMANOS,
            resultado["comparaciones"],
            marker="o",
            label=nombre,
        )

    plt.title("Comparaciones de insertion sort")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/parte3_comparaciones.png")
    plt.close()

    for nombre, resultado in resultados.items():
        plt.plot(
            TAMANOS,
            resultado["tiempos"],
            marker="o",
            label=nombre,
        )

    plt.title("Tiempo de insertion sort")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/parte3_tiempo.png")
    plt.close()


if __name__ == "__main__":
    ejecutar_experimento()