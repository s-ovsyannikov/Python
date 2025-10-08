import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
# параметры
lam = 4.5
# вероятность получить не более 6 звонков
p = poisson.cdf(6, lam)
print(f"P(X ≤ 6) = {p:.3f}")
# визуализация распределения
x = np.arange(0, 15)
pmf = poisson.pmf(x, lam)
plt.bar(x, pmf, color="dodgerblue", alpha=0.7)
plt.title("Распределение Пуассона (λ = 4.5)")
plt.xlabel("Количество звонков")
plt.ylabel("Вероятность")
plt.show() 