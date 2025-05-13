from sympy import symbols, Eq, solve

x, a, b, c = symbols('x a b c')
quadratic_eq = Eq(a*x**2 + b*x + c, 0)
solutions = solve(quadratic_eq, x)
print("Solutions:", solutions)

# For specific values (a=1, b=4, c=3):
specific_solutions = solve(Eq(x**2 + 4*x + 3, 0), x)
print("Specific solutions:", specific_solutions)