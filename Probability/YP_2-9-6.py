import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

data = np.random.poisson(lam=3, size=1000)
plt.hist(data, bins=range(0,10), color="orange", edgecolor="black", alpha=0.7)
plt.title("Симуляция 1000 значений из распределения Пуассона (λ=3)")
plt.xlabel("Количество событий")
plt.ylabel("Частота")
plt.show() 