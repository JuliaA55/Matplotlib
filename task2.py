import numpy as np
import matplotlib.pyplot as plt

mean = 5      
std_dev = 2 

data = np.random.normal(loc=mean, scale=std_dev, size=1000)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black')
plt.title('Гістограма нормального розподілу (μ=5, σ=2)')
plt.xlabel('Значення')
plt.ylabel('Щільність ймовірності')
plt.grid(True)
plt.show()
