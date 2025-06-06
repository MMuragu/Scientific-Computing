import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x, y, label='Sine Wave')
plt.title("Sine Wave Plot")
plt.xlabel("x (radians)")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True)
plt.show()
