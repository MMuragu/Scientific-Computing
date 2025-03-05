import sympy as sp


x = sp.symbols('x')
L = 3*x**2 + 2*x - 5


gradient = sp.diff(L, x)


critical_point = sp.solve(gradient, x)

# Compute the second derivative
second_derivative = sp.diff(gradient, x)

# Check if the critical point is a minimum or maximum
if second_derivative > 0:
    nature = "minimum"
elif second_derivative < 0:
    nature = "maximum"


# Print results
print(f"Loss function: L(x) = {L}")
print(f"First derivative (gradient): = {gradient}")
print(f"Critical point (x when gradient is zero): x = {critical_point[0]}")
print(f"Second derivative: d²L/dx² = {second_derivative}")
print(f"The critical point is a {nature}.")