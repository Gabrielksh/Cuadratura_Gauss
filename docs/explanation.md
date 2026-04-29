# ¿Cómo funciona la Cuadratura Gaussiana?

A diferencia de otros métodos que usan puntos repartidos de forma igual (como la regla del trapecio), la cuadratura Gaussiana es más "inteligente" y eficiente, ya que nos permite trabajar con un muestreo mucho menor al que necesitan otros métodos para darnos un resultado preciso.

Este método elige puntos específicos llamados **nodos** y les asigna una importancia o **peso**. En nuestro script, estos puntos se obtienen a partir de los **polinomios de Legendre**.

La idea matemática es que la integral se aproxima mediante una suma pesada:

$$\int_{a}^{b} f(x) dx \approx \sum_{i=1}^{n} w_i f(x_i)$$

Donde:
* $x_i$ son los nodos (puntos de colocación).
* $w_i$ son los pesos asociados a cada punto.

Al final, lo que hace el código es evaluar la función solo en esos puntos estratégicos, logrando que la aproximación sea muy exacta incluso con un valor de $N$ pequeño.
