import numpy as np
from scipy.stats import randint

# Возможные значения участников (от 1 до 300 включительно)
x = np.arange(1, 301)
# Определяем распределение
disc_uni_dist = randint(1, 301)
# Считаем вероятность попасть в первые 60 участников
cdf = disc_uni_dist.cdf(60)
print(cdf)
