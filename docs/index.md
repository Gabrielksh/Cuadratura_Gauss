# Aproximación Numérica mediante Cuadratura de Gauss-Legendre

## Introducción y Contexto Teórico

En el ámbito de la física computacional y el análisis numérico, se presenta con frecuencia el desafío de resolver integrales que no poseen una solución analítica mediante funciones elementales. Un ejemplo clásico de este fenómeno es la integral de la función $f(x) = \sin(x^2)$, la cual pertenece a la familia de las **Integrales de Fresnel**.

Se ha determinado que estas integrales son fundamentales para describir fenómenos de difracción óptica y propagación de ondas. No obstante, al carecer de una primitiva expresable en términos de funciones básicas, su resolución requiere el empleo de métodos numéricos de alta precisión. Este problema guarda una estrecha relación teórica con otras integrales no elementales de gran importancia en las ciencias exactas, tales como:

* **La integral de Gauss:** $\int e^{-x^2} dx$, esencial en la mecánica estadística y la termodinámica.
* **La integral logarítmica:** $\int \frac{1}{\ln(x)} dx$, de vital importancia en la teoría de números.

## Fundamentos del Método Utilizado

Para el abordaje de este problema, se ha implementado el método de la **Cuadratura de Gauss-Legendre**. A diferencia de los métodos de Newton-Cotes (como las reglas del Trapecio o Simpson), que dependen de puntos equiespaciados, la Cuadratura Gaussiana optimiza la ubicación de los puntos de evaluación para maximizar la exactitud polinomial.

El algoritmo se basa en la utilización de polinomios ortogonales de Legendre, cuyas raíces definen los **nodos** de integración. El cálculo de la integral se aproxima mediante la siguiente suma ponderada:

$$\int_{a}^{b} f(x) dx \approx \sum_{k=1}^{N} w_k f(x_k)$$

donde $x_k$ representa los nodos de colocación y $w_k$ los pesos asociados. Esta técnica permite obtener una convergencia acelerada, especialmente eficiente para funciones con comportamiento oscilatorio como la que se estudia en este proyecto.

## Objetivos del Proyecto

La presente documentación y el código asociado tienen como finalidad cumplir con los siguientes objetivos técnicos:

1.  **Cálculo de la Integral de Fresnel:** Evaluar numéricamente la integral $\int_{0}^{\pi} \sin(x^2) dx$ mediante una implementación propia del algoritmo de Gauss-Legendre.
2.  **Estudio de Convergencia:** Analizar cómo varía la precisión del resultado en función del incremento en el número de puntos de evaluación $N$.
3.  **Generación de Documentación Técnica:** Proveer una referencia clara y reproducible de las funciones, tutoriales de uso y fundamentos teóricos del módulo desarrollado.

## Resultados Esperados

A través de la aplicación estratégica de los nodos de Gauss, se espera que el sistema alcance una estabilidad de alta fidelidad con un valor de convergencia cercano a:

$$I \approx 0.77265$$

Dicho valor será utilizado como el estándar de referencia para validar la eficiencia y la precisión del código implementado frente a las oscilaciones de la función en el intervalo $[0, \pi]$.
