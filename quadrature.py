import numpy as np
import matplotlib.pyplot as plt

def gaussxw(N):
    """
    Calcula nodos y pesos para la cuadratura de Gauss-Legendre.
    
    Args:
        N (int): Número de puntos de integración.
        
    Returns:
        tuple: (nodos, pesos) en el intervalo estándar [-1, 1].
        
    Example:
        >>> x, w = gaussxw(10)
    """
    a = np.linspace(3, 4 * N - 1, N) / (4 * N + 2)
    x = np.cos(np.pi * a + 1 / (8 * N * N * np.tan(a)))
    epsilon = 1e-15
    delta = 1.0
    while delta > epsilon:
        p1 = np.ones(N, float)
        p2 = np.zeros(N, float)
        for j in range(N):
            p3 = p2
            p2 = p1
            p1 = ((2 * j + 1) * x * p2 - j * p3) / (j + 1)
        dp = (N + 1) * (p2 - x * p1) / (1 - x * x)
        dx = p1 / dp
        x -= dx
        delta = max(abs(dx))
    w = 2 * (N + 1) * (N + 1) / (N * N * (1 - x * x) * dp * dp)
    return x, w

def gaussxwab(N, a, b):
    """
    Escala los puntos y pesos al intervalo [a, b].
    
    Args:
        N (int): Número de puntos.
        a (float): Límite inferior.
        b (float): Límite superior.
    """
    x, w = gaussxw(N)
    xp = 0.5 * (b - a) * x + 0.5 * (b + a)
    wp = 0.5 * (b - a) * w
    return xp, wp

def f(x):
    """Función objetivo: sin(x^2)."""
    return np.sin(x**2)

def main():
    """Ejecuta el cálculo y genera el gráfico de convergencia."""
    a, b = 0, np.pi
    N_range = range(1, 51)
    results = []
    
    for n in N_range:
        x, w = gaussxwab(n, a, b)
        results.append(np.sum(w * f(x)))
        
    plt.figure(figsize=(10, 6))
    plt.plot(N_range, results, 'bo-', label='Aproximación')
    plt.axhline(y=0.77265, color='r', linestyle='--', label='Valor de convergencia')
    plt.xlabel('Número de puntos (N)')
    plt.ylabel('Valor de la integral')
    plt.title('Convergencia de la Cuadratura Gaussiana para $sin(x^2)$')
    plt.legend()
    plt.grid(True)
    plt.savefig('docs/img/convergencia.png')
    print(f"Gráfico generado y resultado final (N=50): {results[-1]}")

if __name__ == "__main__":
    main()
