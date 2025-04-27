import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)

y = x**2 * np.sin(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$f(x) = x^2 \cdot \sin(x)$')
plt.title('Графік функції f(x) = x² · sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
