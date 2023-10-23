# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

import numpy as np

# Función objetivo (distribución que queremos muestrear)
def funcion_objetivo(x):
    return np.exp(-x**2) * (4 * x**2 + 1)

# Función de transición (propuesta)
def funcion_transicion(x):
    return x + np.random.normal(0, 0.5)

# Número de muestras a generar
num_muestras = 10000

# Valor inicial
x_actual = 0.0

muestras = []

for _ in range(num_muestras):
    # Generar una propuesta de transición
    x_propuesta = funcion_transicion(x_actual)
    
    # Calcular la razón de aceptación
    razon_aceptacion = funcion_objetivo(x_propuesta) / funcion_objetivo(x_actual)
    
    # Aceptar o rechazar la propuesta
    if np.random.rand() < razon_aceptacion:
        x_actual = x_propuesta
    
    muestras.append(x_actual)

# Imprimir el promedio de las muestras
print("Promedio de las muestras:", np.mean(muestras))
