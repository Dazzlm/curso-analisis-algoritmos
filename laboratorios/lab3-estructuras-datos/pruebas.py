
"""Pruebas automaticas para la lista enlazada y la tabla hash."""

import random

from estructuras import ListaEnlazada, TablaHash


def probar_lista() -> None:
    """Verifica las busquedas exitosas e infructuosas de la lista."""
    lista = ListaEnlazada()
    lista.insertar(1000000010, "en bodega")
    lista.insertar(1000000024, "en reparto")

    assert lista.buscar(1000000010) == "en bodega"
    assert lista.buscar(1000000024) == "en reparto"
    assert lista.buscar(9999999999) is None
    assert lista.tamano == 2


def probar_colisiones() -> None:
    """Verifica tres guias que colisionan en la casilla tres."""
    tabla = TablaHash(7)

    tabla.insertar(10, "en bodega")
    tabla.insertar(24, "en reparto")
    tabla.insertar(17, "entregado")

    assert tabla.hash(10) == 3
    assert tabla.hash(24) == 3
    assert tabla.hash(17) == 3

    assert tabla.buscar(10) == "en bodega"
    assert tabla.buscar(24) == "en reparto"
    assert tabla.buscar(17) == "entregado"
    assert tabla.buscar(99) is None
    assert tabla.casillas[3].tamano == 3
    assert tabla.factor_carga() == 3 / 7


def probar_colecciones_aleatorias() -> None:
    """Compara ambas estructuras con veinte colecciones aleatorias."""
    azar = random.Random(2026)
    estados = ["en bodega", "en reparto", "entregado"]

    for _ in range(20):
        cantidad = azar.randint(20, 100)
        guias = azar.sample(range(10**9, 10**10), cantidad)
        lista = ListaEnlazada()
        tabla = TablaHash(17)
        esperados = {}

        for guia in guias:
            estado = azar.choice(estados)
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)
            esperados[guia] = estado

        for guia, estado in esperados.items():
            assert lista.buscar(guia) == estado
            assert tabla.buscar(guia) == estado

        inexistentes = azar.sample(range(10**9, 10**10), 20)
        for guia in inexistentes:
            if guia not in esperados:
                assert lista.buscar(guia) is None
                assert tabla.buscar(guia) is None

        assert lista.tamano == cantidad
        assert tabla.tamano == cantidad
        assert tabla.factor_carga() == cantidad / 17


def main() -> None:
    """Ejecuta todas las pruebas."""
    probar_lista()
    probar_colisiones()
    probar_colecciones_aleatorias()
    print("Todas las pruebas pasaron correctamente.")


if __name__ == "__main__":
    main()
