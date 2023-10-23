# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install pgmpy

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definir la estructura de la red bayesiana
modelo = BayesianNetwork([('A', 'C'), ('B', 'C')])

# Definir las tablas de probabilidad condicional (CPDs)
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.7], [0.3]])
cpd_c = TabularCPD(variable='C', variable_card=2,
                   values=[[0.9, 0.8, 0.7, 0.1], [0.1, 0.2, 0.3, 0.9]],
                   evidence=['A', 'B'], evidence_card=[2, 2])

# Agregar las CPDs al modelo
modelo.add_cpds(cpd_a, cpd_b, cpd_c)

# Verificar si el modelo es válido
print("El modelo es válido:", modelo.check_model())

# Realizar eliminación de variables
inferencia = VariableElimination(modelo)
resultado = inferencia.query(variables=['C'], evidence={'A': 1, 'B': 0})

print(resultado)
