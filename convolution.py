import numpy as np

a = np.convolve([1,2,3],[0, 1, 0.5, 2, 5], 'same') #same len of the bigger 
print a.tolist()
