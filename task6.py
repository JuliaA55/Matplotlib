import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
f = np.sin(x)
g = np.cos(x)
h = np.sin(x) + np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, f, label='f(x) = sin(x)', color='blue')
plt.plot(x, g, label='g(x) = cos(x)', color='green')
plt.plot(x, h, label='h(x) = sin(x) + cos(x)', color='red')

plt.grid(True)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Графіки трьох функцій')

plt.legend()

plt.show()
