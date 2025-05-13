from sympy import symbols, exp, integrate, oo

x = symbols('x')
g = exp(-x**2)  # e^(-x^2)

integral = integrate(g, (x, -oo, oo))
print("Integral from -∞ to ∞:", integral)