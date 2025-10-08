from scipy.stats import bernoulli
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Моделируем 1000 запусков
data = bernoulli.rvs(size=1000, p=0.7)
# Визуализация
ax = sns.displot(data, kde=False, color="seagreen")
ax.set(
    xlabel="Значение случайной величины (0 - застрял, 1 - успешно)", ylabel="Частота"
)
plt.show()
