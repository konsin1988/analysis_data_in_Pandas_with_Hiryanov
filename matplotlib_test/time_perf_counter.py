import numpy as np
import time

a = list(range(1_000_000))
moment1 = time.perf_counter()
a[::-1] = a
moment2 = time.perf_counter()
print(moment2 - moment1)

b = np.array(range(1_000_000))
moment1 = time.perf_counter()
b[::-1] = b
moment2 = time.perf_counter()
print(moment2 - moment1)
