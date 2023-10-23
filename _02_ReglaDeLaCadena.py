# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

import sympy as sp

# Definir símbolos
x, u = sp.symbols('x u')

# Definir la función compuesta
f = x**2 + x
g = u**3 - u

# Calcular la derivada de f(g(x)) utilizando la Regla de la Cadena
derivative = sp.diff(f.subs(x, g), u)

print(f"La derivada de f(g(x)) es: {derivative}")
