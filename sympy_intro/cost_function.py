import sympy as sp

# Define the symbol and the cost function
x = sp.symbols('x')
C_x = 5*x**3 - 10*x**2 + 4*x + 3

# 1. Find the symbolic derivative of C(x)
derivative = sp.diff(C_x, x)
print("Derivative of C(x):")
print(derivative)


critical_points = sp.solve(derivative, x)
print("\nCritical points:")
print(critical_points)



second_derivative = sp.diff(derivative, x)
print("\nSecond derivative of C(x):")
print(second_derivative)


for point in critical_points:
    second_derivative_at_point = second_derivative.subs(x, point)
    print(f"\nSecond derivative at x = {point}: {second_derivative_at_point}")
    if second_derivative_at_point > 0:
        print(f"The cost function has a local minimum at x = {point}.")
    elif second_derivative_at_point < 0:
        print(f"The cost function has a local maximum at x = {point}.")
