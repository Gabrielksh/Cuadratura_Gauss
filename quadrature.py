"""Módulo para el cálculo de integrales mediante Cuadratura Gaussiana.

Este módulo proporciona herramientas para aproximar integrales definidas
utilizando los pesos y nodos de los polinomios de Legendre.
"""

import numpy as np
import matplotlib.pyplot as plt

def obtener_puntos_y_pesos(grado_n):
    """Genera nodos y pesos de Gauss-Legendre.

    Args:
        grado_n (int): Número de puntos de evaluación.

    Returns:
        tuple: (nodos, pesos) en el intervalo [-1, 1].

    Example:
        >>> nodos, pesos = obtener_puntos_y_pesos(2)
        >>> len(nodos)
        2
    """
    return np.polynomial.legendre.leggauss(grado_n)

def reescalar_espacio_muestreo(nodos_std, pesos_std, a, b):
    """Mapea los nodos y pesos del intervalo [-1, 1] al intervalo [a, b].

    Args:
        nodos_std (ndarray): Nodos originales.
        pesos_std (ndarray): Pesos originales.
        a (float): Límite inferior.
        b (float): Límite superior.

    Returns:
        tuple: (nodos_mapeados, pesos_mapeados).

    Example:
        >>> x, w = reescalar_espacio_muestreo(np.array([-1, 1]), np.array([1, 1]), 0, 10)
        >>> x
        array([ 0., 10.])
    """
    x_m = 0.5 * (b - a) * nodos_std + 0.5 * (b + a)
    w_m = 0.5 * (b - a) * pesos_std
    return x_m, w_m

def calcular_integral_gaussiana(func, lim_inf, lim_sup, orden):
    """Calcula la aproximación numérica de una integral.

    Args:
        func (callable): Función a integrar.
        lim_inf (float): Límite inferior.
        lim_sup (float): Límite superior.
        orden (int): Número de puntos.

    Returns:
        float: Valor aproximado de la integral.

    Example:
        >>> f = lambda x: x**2
        >>> calcular_integral_gaussiana(f, 0, 1, 3)
        0.3333333333333333
    """
    nodos, pesos = obtener_puntos_y_pesos(orden)
    x_i, w_i = reescalar_espacio_muestreo(nodos, pesos, lim_inf, lim_sup)
    return np.sum(w_i * func(x_i))

if __name__ == "__main__":
    f = lambda x: np.sin(x**2)
    a, b = 0, np.pi
    rango_n = range(1, 51)
    estimaciones = [calcular_integral_gaussiana(f, a, b, n) for n in rango_n]
    
    plt.figure(figsize=(10, 6))
    plt.plot(rango_n, estimaciones, 'o-', color='teal', markersize=3)
    plt.title(r'Convergencia de $\int_{0}^{\pi} \sin(x^2) dx$')
    plt.xlabel('N')
    plt.ylabel('I')
    plt.grid(True)
    plt.savefig('convergencia.png')
