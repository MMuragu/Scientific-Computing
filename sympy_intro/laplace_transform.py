import sympy as sp

# Define the symbol and the Laplace Transform function
s = sp.symbols('s')
H_s = 1 / (s**2 + 3*s + 2)

# 1. Factor the denominator symbolically
denominator = s**2 + 3*s + 2
factored_denominator = sp.factor(denominator)
print("Factored denominator:")
print(factored_denominator)

# 2. Compute the inverse Laplace Transform to find h(t)
t = sp.symbols('t', positive=True)
h_t = sp.inverse_laplace_transform(H_s, s, t)
print("\nInverse Laplace Transform h(t):")
print(h_t)

# 3. Find the poles of the system
poles = sp.solve(denominator, s)
print("\nPoles of the system:")
print(poles)