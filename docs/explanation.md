 Matemáticos: Cuadratura de Gauss-Legendre

La Cuadratura Gaussiana es un método de integración numérica que optimiza la precisión al seleccionar estratégicamente los puntos de evaluación (nodos) y sus pesos asociados. A diferencia de las reglas de Newton-Cotes, donde los puntos son equiespaciados, este método permite integrar exactamente polinomios de grado hasta $2n-1$ usando solo $n$ puntos.

## Ortogonalidad y Polinomios de Legendre
El núcleo del método es el uso de los **Polinomios de Legendre** $P_n(x)$, los cuales forman una base ortogonal en el intervalo $[-1, 1]$ bajo la función de peso $w(x) = 1$:

$$\int_{-1}^{1} P_m(x) P_n(x) dx = \frac{2}{2n+1} \delta_{mn}$$

Los nodos de integración $x_i$ son las raíces de $P_n(x)$. Al utilizar estas raíces, el error de la aproximación se minimiza drásticamente.

## Cálculo de Pesos
Los pesos $w_i$ se derivan de la propiedad de que la suma debe ser exacta para polinomios. La fórmula cerrada utilizada es:

$$w_i = \frac{2}{(1-x_i^2) [P'_n(x_i)]^2}$$

Donde $P'_n(x_i)$ es la derivada del polinomio de Legendre evaluada en el nodo $x_i$.

## Transformación de Intervalo (Mapeo Lineal)
Dado que los nodos y pesos estándar están definidos para el intervalo $[-1, 1]$, para resolver nuestra integral en el dominio $[0, \pi]$, aplicamos una transformación lineal (mapeo):

$$x_i = \frac{b-a}{2}\xi_i + \frac{b+a}{2}$$
$$w_i = w_{i,\text{std}} \frac{b-a}{2}$$

Donde $\xi_i$ representa el nodo en el intervalo estándar y $x_i$ el nodo escalado.

## La Integral de Fresnel
El problema a resolver, $I = \int_{0}^{\pi} \sin(x^2) dx$, es una variante de las **integrales de Fresnel**. Estas funciones son fundamentales en la óptica física para describir patrones de difracción. Debido a su naturaleza oscilatoria y la carencia de una primitiva elemental, la Cuadratura Gaussiana es el método más eficiente para alcanzar la convergencia con un costo computacional mínimo.
