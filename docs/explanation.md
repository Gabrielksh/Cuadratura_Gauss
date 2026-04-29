# Investigación Teórica: El Desafío de las Integrales de Fresnel

En este apartado se documenta la naturaleza del problema matemático abordado y la justificación técnica detrás de la elección del método numérico implementado.

## 1. Caracterización del Problema
La función objeto de estudio es $f(x) = \sin(x^2)$, cuya integración en el dominio $[0, \pi]$ da lugar a una variante de las denominadas **Integrales de Fresnel**. 

Se ha determinado que estas funciones poseen una particularidad fundamental: **carecen de una primitiva elemental**. Esto implica que el cálculo de la integral no puede resolverse mediante métodos analíticos tradicionales (como la sustitución o la integración por partes), lo que hace imperativo el uso de herramientas de la física computacional para obtener una aproximación numérica precisa.

## 2. Aplicaciones en la Ciencia y la Ingeniería
La relevancia de este problema trasciende el ámbito teórico. Se ha identificado que estas integrales son esenciales en áreas como:
* **Óptica Física:** Se utilizan para modelar los patrones de difracción de la luz al atravesar una rendija.
* **Diseño de Infraestructura:** En la ingeniería civil, se emplean para el cálculo de curvas de transición (clotoides), garantizando cambios de dirección seguros en carreteras y vías férreas.

## 3. Metodología: Cuadratura de Gauss-Legendre
Para resolver la carencia de una solución analítica, se emplea el método de la **Cuadratura Gaussiana**. A diferencia de las reglas de Newton-Cotes, que utilizan intervalos equiespaciados, este método optimiza la precisión mediante la selección estratégica de puntos de evaluación denominados **nodos**.

### Componentes del Método:
* **Nodos ($x_i$):** Se definen como las raíces de los Polinomios de Legendre. Estos puntos representan las ubicaciones óptimas donde se debe "muestrear" la función para minimizar el error.
* **Pesos ($w_i$):** Representan la importancia relativa asignada a cada nodo para garantizar que la suma ponderada sea exacta para polinomios de grado hasta $2n-1$.
* **Mapeo Lineal:** Dado que los nodos y pesos se calculan originalmente para el intervalo estándar $[-1, 1]$, se aplica una transformación de coordenadas para escalar el método al intervalo físico requerido de $[0, \pi]$.

## 4. Análisis de Convergencia y Eficiencia
Debido a la naturaleza oscilatoria de $\sin(x^2)$, los métodos de orden inferior suelen requerir una densidad de puntos muy elevada. Sin embargo, se observa que la Cuadratura Gaussiana logra una estabilidad de cinco cifras decimales con un número reducido de evaluaciones.


Al aplicar el método, se alcanza un valor de convergencia de aproximadamente **0.77265**. Este resultado confirma que la técnica empleada es la herramienta óptima para abordar funciones con comportamientos complejos donde los recursos computacionales deben ser utilizados con eficiencia.
