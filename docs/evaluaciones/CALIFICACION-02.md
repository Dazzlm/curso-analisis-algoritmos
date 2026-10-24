# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Daniel Felipe Marín Marín · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `54686c0`

Muy buen trabajo: el código es correcto y el informe responde casi todo lo pedido.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 17 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 21 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **90 / 100** |
| **Nota (0–5)** | **4.50** |

## 1. Corrección conceptual (17 / 20)
**Lo que hizo bien:**
- Identificó que divide y vencerás empieza a ganar desde n = 100 y explicó por qué en listas pequeñas la recursión cuesta más.
- Comparó correctamente con hallar el máximo de un arreglo: combinar cuesta `Θ(1)`, la recurrencia da `Θ(n)` y dividir no ayuda.
- Recomendó divide y vencerás y declaró sus cifras como estimaciones, sin usar una regla de tres lineal.

**Lo que puede mejorar:**
- En la pregunta 5 escribió "39.863 segundos" y luego "unas 11 horas": las dos cifras no coinciden en unidades (39.863 segundos son unas 11 horas, pero el número está mal puesto). Revise las unidades al reportar.

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Planteó `T(n) = 2T(n/2) + Θ(n)` explicando de dónde sale cada término.
- Resolvió con el método maestro y verificó la condición del caso 2.

**Lo que puede mejorar:**
- La justificación del `Θ(n²)` de la fuerza bruta es muy breve; podría mostrar la suma `n(n+1)/2` y por qué domina `n²`.

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden en listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta y no modifica la lista.
- Tiene type hints y docstrings Google-style, y el código cumple PEP 8.

**Lo que puede mejorar:**
- En los docstrings de `suma_cruzada` y `subarreglo_maximo` conviene indicar que los índices son inclusivos, como en el enunciado.

## 4. Calidad del análisis de las gráficas (21 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y seis tamaños.
- Calculó el factor al duplicar n (500 a 1000) para ambos algoritmos y lo comparó con lo esperado.
- Incluyó una tabla con los valores medidos y usó cifras reales en sus afirmaciones.

**Lo que puede mejorar:**
- En divide y vencerás obtuvo un factor de 0.92 (esperaba cerca de 2.22). Lo atribuyó al ruido, pero no repitió las mediciones para comprobarlo. Medir varias veces y promediar habría dado un factor más creíble.
- El informe dice que midió una sola vez por tamaño; la nota sobre cómo midió podría ser más completa.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Carpeta en la ubicación acordada (`laboratorios/lab2-divide-y-vencer/`) con todos los archivos del entregable.
- README en el orden pedido, con nombre, instrucciones de reproducción, enlaces al código y gráfica visible.
- Tres commits descriptivos del laboratorio.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos dan siempre la misma suma y `medicion.py` corre sin errores y genera la gráfica.

## Para el próximo laboratorio
- Repita cada medición varias veces y grafique el promedio o la mediana.
- Revise las unidades y las cifras antes de escribirlas en el informe.
- Desarrolle un poco más la justificación de las complejidades teóricas.
