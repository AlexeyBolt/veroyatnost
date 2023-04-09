import scipy.stats as stats
import numpy as np
arr = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
mean_arr = np.mean(arr)
print(mean_arr)
D = np.var(arr, ddof=1)
print(D)
t = stats.t.ppf(0.975, 9)
print(t)
print(mean_arr - t * np.sqrt(D/10))
print(mean_arr + t * np.sqrt(D/10))
print(' 95%-й доверительный интервал для истинного значения IQ: (110.55, 125.64)')