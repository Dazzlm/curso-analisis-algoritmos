# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Daniel Felipe Marín Marín · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `4602dcc`

Muy buen trabajo: el código funciona y el informe cubre las cuatro partes.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 17 / 25 |
| Corrección de la implementación | 18 / 20 |
| Calidad del análisis de las gráficas | 17 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **82 / 100** |
| **Nota (0–5)** | **4.10** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Separa bien "correcto" de "rápido" y nombra la ventana de cuatro horas como la restricción que no se cumple.
- Explica que el crecimiento cuadrático no se arregla con un servidor más veloz.
- En la Parte 2 relaciona el tiempo con el gasto de energía que se acumula cada madrugada.
- Identifica perjuicios concretos (pacientes de riesgo alto, operadores del centro de contacto) y dice quién asume el costo.
- Señala que el orden de la lista decide a quién se llama primero.

**Lo que puede mejorar:**
- El segundo ejemplo (el buscador) es muy breve: falta decir qué datos procesa de verdad y por qué fallaría con un servidor más rápido.
- Explique con más detalle por qué duplicar la velocidad solo ahorra la mitad del tiempo mientras que el problema crece mucho más rápido.

## 2. Calidad de la explicación teórica (17 / 25)
**Lo que hizo bien:**
- Define peor caso, mejor caso y caso promedio, y justifica que usaría el peor caso para decidir.
- Deja escrita la predicción antes del experimento y la contrasta después.
- Plantea la recurrencia de merge sort, explica cada término y la resuelve con el método maestro verificando que cae en el caso 2.
- Incluye la tabla de complejidades.

**Lo que puede mejorar:**
- Para insertion sort no hizo el cálculo línea a línea que se pedía: faltó indicar cuántas veces se ejecuta cada línea de su código y sumar esos costos. Solo explicó el resultado en palabras.
- En las definiciones de los casos falta precisar sobre qué conjunto de entradas se toma el máximo, el mínimo y el promedio.

## 3. Corrección de la implementación (18 / 20)
**Lo que hizo bien:**
- Ambos algoritmos ordenan bien los tres escenarios, no cambian la lista original y cuentan las comparaciones entre elementos (en una lista ya ordenada da n - 1, como debe ser).
- Merge sort tiene su propia mezcla recursiva y no se usa `sorted()` ni `sort()`.
- Los generadores dan listas del tamaño pedido, sin repetidos y con semilla.
- Hay docstrings y type hints casi en todo el código, y el estilo es limpio.

**Lo que puede mejorar:**
- La función `medir` de la Parte 4 no tiene type hint en el parámetro `algoritmo`.
- Algunos docstrings no siguen exactamente el texto del enunciado.

## 4. Calidad del análisis de las gráficas (17 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes con unidades y leyenda, y los escenarios van en los mismos ejes.
- Identifica con datos el peor caso (inverso), el mejor (casi ordenado) y el promedio (aleatorio).
- Concluye que merge sort conviene, explica lo que hace cada curva y lo relaciona con las complejidades.
- Explica por qué merge sort es más lento con n pequeño.
- Estima el tiempo para 1.200.000 registros, lo declara como estimación y explica el razonamiento.

**Lo que puede mejorar:**
- No dice cómo midió (por ejemplo, que promedió tres repeticiones).
- Al responder la propuesta del servidor doble, compare directamente: aun con la mitad del tiempo, insertion sort quedaría en unas 8 horas, fuera de la ventana.
- Falta discutir la estabilidad o el riesgo de que el escenario B deje de ser casi ordenado.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Estructura correcta, informe por partes, gráficas visibles y enlaces al código en las partes prácticas.
- Instrucciones de reproducción claras y seis commits con mensajes descriptivos.

**Lo que puede mejorar:**
- Un mensaje de commit quedó incompleto ("Agrega README para el laboratorio , ..."). Cuide que digan con claridad qué cambió.

## ¿El código funciona?
Sí. Los dos scripts corren sin errores, ordenan correctamente y generan las tres gráficas.

## Para el próximo laboratorio
- Cuando se pida un cálculo línea a línea, escriba una tabla con cuántas veces se ejecuta cada línea y la suma final.
- Defina cada caso diciendo sobre qué conjunto de entradas se toma el máximo, el mínimo o el promedio.
- Use ejemplos propios con más datos concretos (qué se procesa, cuánto y qué restricción falla).
- Agregue type hints a todos los parámetros.
- Cuente en el informe cómo hizo las mediciones.
