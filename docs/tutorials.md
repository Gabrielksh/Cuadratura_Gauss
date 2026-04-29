# Guía de Uso del Módulo

En esta sección se explica cómo implementar el código y se proporcionan los pasos necesarios para asegurar que todo funcione sin problemas.

### 1. Requisitos previos
Para que el script funcione correctamente, se requiere tener instalada la librería `numpy`, la cual se encarga de gestionar los arreglos numéricos y los polinomios de Legendre.

### 2. Importación y configuración
Es necesario asegurarse de que el archivo `quadrature.py` se encuentre en la misma carpeta que el script de trabajo. Posteriormente, se debe importar la función principal y definir la función matemática que se desea integrar.

### 3. Ejemplo práctico: Integral de una parábola
A continuación se muestra un ejemplo de cómo calcular la integral de una función cuadrática $f(x) = x^2$ en el intervalo de 0 a 1:

### 4. Consideraciones:
Se debe tomar en cuenta que al aumentar el valor de n_puntos, la aproximación tiende a ser más exacta. Para funciones con mayor grado de oscilación, se recomienda utilizar un valor de $N$ más elevado para garantizar la convergencia del resultado.

```python
import numpy as np
from quadrature import calcular_integral_gaussiana

# 1. Definición de la función mediante una expresión lambda
f = lambda x: x**2

# 2. Definición de los límites (a, b) y el número de puntos (N)
# Nota: Para una función polinomial simple, con N=10 se obtiene alta precisión.
lim_inferior = 0
lim_superior = 1
n_puntos = 10

# 3. Llamada a la función de integración
resultado = calcular_integral_gaussiana(f, lim_inferior, lim_superior, n_puntos)

print(f"El resultado de la integral es: {resultado}")

