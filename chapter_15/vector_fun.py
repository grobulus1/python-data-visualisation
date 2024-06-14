import numpy as np
nums_1 = [5, 4, 3, 2, 1]
vec_1 = np.array(nums_1)
mask = np.array([5, 5, 5, 5, 5])
nums_1 = nums_1 * mask
print(nums_1)