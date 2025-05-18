import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

# 5 noduri echidistante între -8 și 8
x_nodes = np.linspace(-8, 8, 5)
y_nodes = 1 / (1 + x_nodes**2)

# Polinomul de interpolare
poly = lagrange(x_nodes, y_nodes)

# Afișare coeficienți
print("Polinomul Lagrange pentru 5 noduri:")
print(np.poly1d(poly))

# Reprezentare grafică
x = np.linspace(-8, 8, 400)
y = 1 / (1 + x**2)
y_interp = poly(x)

plt.plot(x, y, label="f(x) = 1 / (1 + x^2)")
plt.plot(x, y_interp, label="Interpolare Lagrange (5 noduri)", linestyle='--')
plt.scatter(x_nodes, y_nodes, color='red')
plt.legend()
plt.title("Interpolare Lagrange cu 5 noduri")
plt.grid(True)
plt.show()
