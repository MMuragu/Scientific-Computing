from sympy import symbols, diff, solve

x = symbols('x')
f = x**3 - 2*x**2 + x - 3

# First derivative
f_prime = diff(f, x)
print("First derivative:", f_prime)

# Critical points
critical_points = solve(f_prime, x)
print("Critical points:", critical_points)

# Second derivative test
f_double_prime = diff(f_prime, x)
for point in critical_points:
    second_deriv = f_double_prime.subs(x, point)
    if second_deriv > 0:
        print(f"Point {point} is a local minimum")
    elif second_deriv < 0:
        print(f"Point {point} is a local maximum")
    else:
        print(f"Point {point} is a saddle point")