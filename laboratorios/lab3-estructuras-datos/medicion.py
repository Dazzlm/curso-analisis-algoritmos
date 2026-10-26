
"""Experimentos de rendimiento para la lista y la tabla hash."""

import random
import time
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash


SEMILLA = 2026
CANTIDAD_BUSQUEDAS = 200
REPETICIONES = 3
CARPETA_GRAFICAS = Path(__file__).parent / "graficas"


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: Guias almacenadas en las estructuras.
        cantidad: Cantidad de guias inexistentes que generar.
        semilla: Semilla del generador aleatorio.

    Returns:
        Una lista de guias inexistentes.
    """
    azar = random.Random(semilla)
    inexistentes = []

    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)

    return inexistentes


def generar_guias(cantidad: int) -> list[int]:
    """Genera guias distintas y reproducibles de diez digitos.

    Args:
        cantidad: Numero de guias que generar.

    Returns:
        Una lista de guias unicas.
    """
    azar = random.Random(SEMILLA + cantidad)
    return azar.sample(range(10**9, 10**10), cantidad)


def siguiente_primo(numero: int) -> int:
    """Devuelve el primer numero primo mayor o igual al recibido.

    Args:
        numero: Numero inicial.

    Returns:
        El primer primo encontrado.
    """
    candidato = max(2, numero)

    while True:
        es_primo = True
        divisor = 2

        while divisor * divisor <= candidato:
            if candidato % divisor == 0:
                es_primo = False
                break
            divisor += 1

        if es_primo:
            return candidato

        candidato += 1


def medir_busquedas(
    estructura: ListaEnlazada | TablaHash, consultas: list[int]
) -> float:
    """Mide el tiempo promedio de busqueda en segundos.

    Args:
        estructura: Lista enlazada o tabla hash.
        consultas: Guias que se van a buscar.

    Returns:
        Tiempo promedio por busqueda, en segundos.
    """
    tiempos = []

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()

        for guia in consultas:
            estructura.buscar(guia)

        fin = time.perf_counter()
        tiempos.append((fin - inicio) / len(consultas))

    return sum(tiempos) / len(tiempos)


def verificar_equivalencia(
    lista: ListaEnlazada,
    tabla: TablaHash,
    guias: list[int],
) -> None:
    """Comprueba que ambas estructuras devuelvan los mismos estados.

    Args:
        lista: Lista enlazada construida.
        tabla: Tabla hash construida.
        guias: Guias existentes que se van a comprobar.
    """
    for guia in guias[:100]:
        assert lista.buscar(guia) == tabla.buscar(guia)


def experimento_a() -> None:
    """Compara ambas estructuras para diferentes cantidades de guias."""
    tamanos = [100, 500, 1000, 5000, 20000, 50000]
    tiempos_lista = []
    tiempos_tabla = []

    print("\nEXPERIMENTO A: lista frente a tabla")
    print("n | m | alfa | lista (s/busqueda) | tabla (s/busqueda)")

    for n in tamanos:
        guias = generar_guias(n)
        existentes = set(guias)
        consultas = generar_guias_inexistentes(
            existentes, CANTIDAD_BUSQUEDAS, SEMILLA
        )

        m = siguiente_primo(max(2, n // 2))
        lista = ListaEnlazada()
        tabla = TablaHash(m)

        for guia in guias:
            lista.insertar(guia, "en bodega")
            tabla.insertar(guia, "en bodega")

        verificar_equivalencia(lista, tabla, guias)

        tiempo_lista = medir_busquedas(lista, consultas)
        tiempo_tabla = medir_busquedas(tabla, consultas)

        tiempos_lista.append(tiempo_lista)
        tiempos_tabla.append(tiempo_tabla)

        print(
            f"{n} | {m} | {tabla.factor_carga():.3f} | "
            f"{tiempo_lista:.8e} | {tiempo_tabla:.8e}"
        )

    print("\nFactores de crecimiento entre valores consecutivos de n:")
    for i in range(1, len(tamanos)):
        factor_lista = tiempos_lista[i] / tiempos_lista[i - 1]
        factor_tabla = tiempos_tabla[i] / tiempos_tabla[i - 1]
        factor_n = tamanos[i] / tamanos[i - 1]

        print(
            f"{tamanos[i - 1]} -> {tamanos[i]} "
            f"(n x {factor_n:.2f}): "
            f"lista x {factor_lista:.2f}; "
            f"tabla x {factor_tabla:.2f}"
        )

    plt.figure(figsize=(9, 5))
    plt.plot(tamanos, tiempos_lista, marker="o", label="Lista enlazada")
    plt.plot(tamanos, tiempos_tabla, marker="o", label="Tabla hash")
    plt.title("Tiempo de busqueda frente al numero de guias")
    plt.xlabel("Numero de guias (n)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.yscale("log")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "lista_vs_tabla.png", dpi=150)
    plt.close()


def experimento_b() -> None:
    """Mide el efecto del factor de carga sobre la tabla hash."""
    n = 20000
    alfas_objetivo = [0.5, 1, 4, 10]
    guias = generar_guias(n)
    existentes = set(guias)
    consultas = generar_guias_inexistentes(
        existentes, CANTIDAD_BUSQUEDAS, SEMILLA + 1
    )

    lista = ListaEnlazada()
    for guia in guias:
        lista.insertar(guia, "en bodega")

    tiempos = []
    alfas_reales = []

    print("\nEXPERIMENTO B: efecto del factor de carga")
    print("n | m | alfa real | tabla (s/busqueda)")

    for alfa in alfas_objetivo:
        m = max(1, round(n / alfa))
        tabla = TablaHash(m)

        for guia in guias:
            tabla.insertar(guia, "en bodega")

        verificar_equivalencia(lista, tabla, guias)

        tiempo_tabla = medir_busquedas(tabla, consultas)
        alfa_real = tabla.factor_carga()

        alfas_reales.append(alfa_real)
        tiempos.append(tiempo_tabla)

        print(
            f"{n} | {m} | {alfa_real:.3f} | "
            f"{tiempo_tabla:.8e}"
        )

    plt.figure(figsize=(9, 5))
    plt.plot(alfas_reales, tiempos, marker="o", label="Tabla hash")
    plt.title("Tiempo de busqueda frente al factor de carga")
    plt.xlabel("Factor de carga (alfa = n / m)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "tiempo_vs_alfa.png", dpi=150)
    plt.close()


def main() -> None:
    """Ejecuta los dos experimentos y guarda sus graficas."""
    CARPETA_GRAFICAS.mkdir(parents=True, exist_ok=True)
    experimento_a()
    experimento_b()
    print("\nGraficas guardadas en la carpeta graficas/.")


if __name__ == "__main__":
    main()
