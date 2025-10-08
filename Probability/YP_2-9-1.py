import numpy as np
from scipy.stats import randint
# Возможные значения
x = np.arange(1, 9)
# Определяем распределение
disc_uni_dist = randint(1, 9)
# Вероятности для каждого значения
pmf = disc_uni_dist.pmf(x)
print(pmf) 
