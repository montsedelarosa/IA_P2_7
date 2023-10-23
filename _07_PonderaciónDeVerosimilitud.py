# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

import numpy as np

# Definir la red bayesiana con sus probabilidades
# Las probabilidades se definen como P(X|Padres(X)), donde X es el nodo y Padres(X) son sus padres.
# En este ejemplo, usamos valores arbitrarios.
P_A = 0.6
P_B_given_A = {0: 0.7, 1: 0.3}
P_C_given_B = {0: 0.8, 1: 0.2}

# Número de muestras a generar
num_muestras = 10000

# Contadores para contar las muestras que cumplen con la evidencia
contador_c = 0

for _ in range(num_muestras):
    # Generar muestras para A y B usando sus distribuciones
    A = np.random.choice([0, 1], p=[1 - P_A, P_A])
    B = np.random.choice([0, 1], p=[1 - P_B_given_A[A], P_B_given_A[A]])
    
    # Verificar si las muestras cumplen con la evidencia
    if A == 1 and B == 0:
        # Generar una muestra para C dado B
        C = np.random.choice([0, 1], p=[1 - P_C_given_B[B], P_C_given_B[B]])
        if C == 1:
            contador_c += 1

# Calcular la probabilidad estimada
probabilidad_estimada = contador_c / num_muestras

print("Probabilidad estimada de C dado A=1 y B=0:", probabilidad_estimada)
