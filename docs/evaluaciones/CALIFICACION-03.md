# Retroalimentación — Laboratorio 03 · Estructuras de datos

**Estudiante:** Daniel Felipe Marin Marin · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `2ba1c70`

Excelente trabajo: entrega completa, ordenada y con análisis apoyado en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 20 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 25 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **100 / 100** |
| **Nota (0–5)** | **5.00** |

## 1. Corrección conceptual (20 / 20)
**Lo que hizo bien:**
- Explica bien qué es una colisión y por qué ocurre aunque haya más casillas que guías, con el ejemplo de 10, 24 y 17 con m = 7.
- Compara encadenamiento y direccionamiento abierto con ventajas y costos de cada uno.
- Justifica por qué la tabla no sirve para rangos y estima la altura del árbol degenerado y del equilibrado con sus comparaciones.
- La recomendación (tabla hash más árbol equilibrado) es clara y la estimación para 5.000.000 de envíos está declarada como estimación y razonada.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justifica el Θ(n) de la lista y el Θ(1 + α) de la tabla, nombra el supuesto de hash uniforme simple y explica que, si todas las guías caen en una casilla, la tabla se comporta como una lista con costo Θ(n).

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Lista y tabla devuelven el estado correcto en búsquedas exitosas e infructuosas; la colisión con m = 7 y `factor_carga` funcionan.
- La tabla reutiliza `ListaEnlazada`, sin `dict`, `set` ni `hash()`, y `buscar` es iterativa.
- Las pruebas comparan 20 colecciones aleatorias y todas pasan.
- Todas las funciones tienen *docstrings* con `Args` y `Returns`, *type hints* y dos líneas en blanco entre funciones.

## 4. Calidad del análisis de las gráficas (25 / 25)
**Lo que hizo bien:**
- Ambas gráficas tienen título, ejes rotulados y leyenda; la primera cubre seis valores de n y la segunda cuatro valores de α.
- Los factores de crecimiento que calcula (por ejemplo, lista × 2,69 y tabla × 1,02 entre 20.000 y 50.000) coinciden con lo que muestran las gráficas.
- Interpreta con criterio que el tiempo en función de α sube más despacio de lo esperado por el costo fijo, y lo contrasta con Θ(1 + α).

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- El laboratorio está en `laboratorios/lab3-estructuras-datos/`, ubicación válida, con todos los archivos pedidos.
- El informe sigue el orden pedido, enlaza el código en cada parte, incrusta las gráficas con ruta relativa que funciona y trae instrucciones de reproducción.
- Hay tres commits descriptivos del laboratorio.

## ¿El código funciona?
Sí. Las pruebas pasan sin errores y `medicion.py` corre completo y genera las dos gráficas. Lista y tabla coinciden en todas las comprobaciones.
