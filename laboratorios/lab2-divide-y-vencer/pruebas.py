import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def probar_serie_principal() -> None:
    serie = [-3, 5, -2, 8, -6, 3, 9, -4]

    resultado_bruta = subarreglo_fuerza_bruta(serie)
    resultado_divide = subarreglo_maximo(
        serie,
        0,
        len(serie) - 1,
    )

    assert resultado_bruta[2] == 17
    assert resultado_divide[2] == 17


def probar_un_elemento() -> None:
    serie = [7]

    assert subarreglo_fuerza_bruta(serie)[2] == 7
    assert subarreglo_maximo(serie, 0, 0)[2] == 7


def probar_todos_negativos() -> None:
    serie = [-8, -3, -10, -2]

    assert subarreglo_fuerza_bruta(serie)[2] == -2
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == -2


def probar_todos_positivos() -> None:
    serie = [2, 4, 6, 3]

    assert subarreglo_fuerza_bruta(serie)[2] == 15
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 15


def probar_caso_cruzado() -> None:
    serie = [-10, 4, 5, -2, 3, -20]

    resultado_bruta = subarreglo_fuerza_bruta(serie)
    resultado_divide = subarreglo_maximo(
        serie,
        0,
        len(serie) - 1,
    )

    assert resultado_bruta[2] == 10
    assert resultado_divide[2] == 10


def probar_listas_aleatorias() -> None:
    random.seed(42)

    for _ in range(20):
        serie = [
            random.randint(-20, 20)
            for _ in range(random.randint(1, 30))
        ]

        resultado_bruta = subarreglo_fuerza_bruta(serie)
        resultado_divide = subarreglo_maximo(
            serie,
            0,
            len(serie) - 1,
        )

        assert resultado_bruta[2] == resultado_divide[2]


def main() -> None:
    probar_serie_principal()
    probar_un_elemento()
    probar_todos_negativos()
    probar_todos_positivos()
    probar_caso_cruzado()
    probar_listas_aleatorias()

    print("Todas las pruebas pasaron correctamente.")


if __name__ == "__main__":
    main()