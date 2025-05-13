import numpy as np

def integrate_trapezoid(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    return (h/2) * (y[0] + 2*sum(y[1:-1]) + y[-1])

# Function and integral
result = integrate_trapezoid(lambda x: x**2, 0, 2, 100)
print("Estimated integral:", result)
#More trapezoids (larger n) mean better accuracy. Here, n=100 gives a good approximation.