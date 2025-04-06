# python .\10_popular_pyton_packages\12_numpy.py

import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)  # [[1 2 3]
# [4 5 6]]
print(type(array))  # <class 'numpy.ndarray'>

array = np.zeros((3, 4))
print(array)  # [[0. 0. 0. 0.]
# [0. 0. 0. 0.]
# [0. 0. 0. 0.]]

array = np.zeros((3, 4), dtype=int)
print(array)  # [[0 0 0 0]
# [0 0 0 0]
# [0 0 0 0]]

array = np.random.random((3, 4))  # array with random numbers
print(array)
