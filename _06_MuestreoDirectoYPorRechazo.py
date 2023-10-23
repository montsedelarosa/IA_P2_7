# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

#Muestreo directo

import numpy as np

# Parámetros de la distribución normal
media = 0
desviacion_estandar = 1
tamaño_muestra = 100

# Generar muestras de una distribución normal
muestras = np.random.normal(media, desviacion_estandar, tamaño_muestra)

# Imprimir las primeras 10 muestras
print("Muestras generadas:")
print(muestras[:10])

#Muestreo por rechazo

import numpy as np

# Función de densidad de probabilidad de Cauchy
def cauchy(x, x0, gamma):
    return 1 / (np.pi * gamma * (1 + ((x - x0) / gamma) ** 2))

# Parámetros de la distribución de Cauchy
x0 = 0
gamma = 1
tamaño_muestra = 1000

muestras_aceptadas = []

# Generar muestras de la distribución de Cauchy utilizando el muestreo por rechazo
for _ in range(tamaño_muestra):
    propuesta = np.random.uniform(x0 - 5 * gamma, x0 + 5 * gamma)
    aceptacion = np.random.uniform(0, 1)
    if aceptacion < cauchy(propuesta, x0, gamma):
        muestras_aceptadas.append(propuesta)

# Imprimir las primeras 10 muestras aceptadas
print("Muestras generadas por rechazo:")
print(muestras_aceptadas[:10])
