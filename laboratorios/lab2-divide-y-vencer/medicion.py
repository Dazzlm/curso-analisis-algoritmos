import os
import random
import time

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def medir_tiempo() -> None:
    """Mide y grafica el tiempo de ambos algoritmos."""
    tamanos = [10, 50, 100, 500, 1000, 4000]

    tiempos_bruta = []
    tiempos_divide = []

    random.seed(42)

    for n in tamanos:
        valores = [random.randint(-100, 100) for _ in range(n)]

        inicio = time.perf_counter()
        resultado_bruta = subarreglo_fuerza_bruta(valores)
        fin = time.perf_counter()
        tiempo_bruta = fin - inicio

        inicio = time.perf_counter()
        resultado_divide = subarreglo_maximo(
            valores,
            0,
            len(valores) - 1,
        )
        fin = time.perf_counter()
        tiempo_divide = fin - inicio

        assert resultado_bruta[2] == resultado_divide[2]

        tiempos_bruta.append(tiempo_bruta)
        tiempos_divide.append(tiempo_divide)

        print(
            f"n={n}: "
            f"fuerza bruta={tiempo_bruta:.6f}s, "
            f"divide y venceras={tiempo_divide:.6f}s"
        )

    os.makedirs("graficas", exist_ok=True)

    plt.figure(figsize=(9, 6))

    plt.plot(
        tamanos,
        tiempos_bruta,
        marker="o",
        label="Fuerza bruta",
    )

    plt.plot(
        tamanos,
        tiempos_divide,
        marker="o",
        label="Divide y vencerás",
    )

    plt.title("Tiempo de ejecución vs tamaño de entrada")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)

    plt.savefig(
        "graficas/tiempo_vs_n.png",
        dpi=150,
        bbox_inches="tight",
    )

    plt.show()


if __name__ == "__main__":
    medir_tiempo()