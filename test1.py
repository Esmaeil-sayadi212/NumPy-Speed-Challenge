import time
import numpy as np

size_vector = 1000000


def list_view():
    t1 = time.time()
    i1 = range(size_vector)
    i2 = range(size_vector)
    summation = [i1[i] + i2[i] for i in range(len(i1))]
    return time.time() - t1


def numpy_view():
    t1 = time.time()
    n1 = np.arange(size_vector)
    n2 = np.arange(size_vector)
    summation = n1 + n2
    return time.time() - t1


t_list_view = list_view()
t_numpy_view = numpy_view()
print("numpy is " + str(t_list_view / t_numpy_view) + "faster than list")
