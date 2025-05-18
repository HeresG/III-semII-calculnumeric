#trebuie să ilustrăm grafic polinoamele de interpolare Lagrange construite la punctul (b), adică pentru:
#5 noduri
#10 noduri
#15 noduri


import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

# Funcția dată
def f(x):
    return 1 / (1 + x**2)

# Punctele x pentru desen
x_vals = np.linspace(-8, 8, 1000)
f_vals = f(x_vals)

# Numar de noduri pentru test
noduri_list = [5, 10, 15]
colors = ['red', 'green', 'blue']
labels = []

plt.figure(figsize=(10, 6))
plt.plot(x_vals, f_vals, 'k-', label='f(x) = 1 / (1 + x²)', linewidth=2)

# Adăugăm polinoamele de interpolare pentru 5, 10, 15 noduri
for i, n in enumerate(noduri_list):
    x_nodes = np.linspace(-8, 8, n)
    y_nodes = f(x_nodes)
    poly = lagrange(x_nodes, y_nodes)
    y_interp = poly(x_vals)
    plt.plot(x_vals, y_interp, linestyle='--', color=colors[i],
             label=f'Interpolare Lagrange ({n} noduri)')

plt.title("Interpolare Lagrange cu 5, 10 și 15 noduri")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
