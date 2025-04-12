
"""
NumPy is used to work with arrays. The array object in NumPy is called ndarray.
We can create a NumPy ndarray object by using the array() function.
"""

import numpy as np
arr=np.array([1,2,3,4])

print(arr)
print(type(arr))


"""
Check Number of Dimensions
"""
import numpy as np
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


"""
Higher Dimensional Arrays
"""

import numpy as np
a = np.array([1, 2, 3, 4, 5],dtype=str,ndmin=5)
print(a.ndim)

