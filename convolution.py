import numpy as np

a = np.convolve([1,2,3],[0, 1, 0.5, 2, 5], 'same')
print a.tolist()
