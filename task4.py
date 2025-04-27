import numpy as np
import matplotlib.pyplot as plt

fruits = ['Яблука', 'Банани', 'Апельсини', 'Груші']

np.random.seed(42)
apple_weights = np.random.normal(loc=180, scale=20, size=100)
banana_weights = np.random.normal(loc=120, scale=15, size=100)
orange_weights = np.random.normal(loc=150, scale=18, size=100)
pear_weights = np.random.normal(loc=170, scale=22, size=100)

data = [apple_weights, banana_weights, orange_weights, pear_weights]

plt.figure(figsize=(10, 6))
plt.boxplot(data, labels=fruits)
plt.title('Box-Plot маси фруктів')
plt.ylabel('Маса (г)')
plt.grid(True)
plt.show()
