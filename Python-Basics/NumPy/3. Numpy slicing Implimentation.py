import numpy as np
"""
Slicing in python means taking elements from one given index to another given index.
We pass slice instead of index like this: [start:end].
We can also define the step, like this: [start:end:step].
If we don't pass start its considered 0
If we don't pass end its considered length of array in that dimension
If we don't pass step its considered 1
"""


print("_______________Slicig of 1d array_______________")
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print("Actual Array : ",arr)
print("arr[0:1]=",arr[0:1])
print("If we don't pass start its considered 0. e.g. arr[:1]=",arr[:1])
print("If we don't pass end its considered length of array in that dimension. e.g. arr[1:]=",arr[1:])
print("arr[0::2]=",arr[0::2])
print("arr[::1]=",arr[::1])
print("arr[::-1]=",arr[::-1])

print("\n\n\n\n\n_______________Slicig of 2d array_______________\n\n\n\n\n")


print("_______________From the second element, slice elements from index 1 to index 4 (not included):_______________",sep="\n")
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Actual Array : ",arr,sep="\n")
print("arr[1, 1:4: ",arr[1, 1:4])

print("_______________From the second element, slice elements from index 1 to index 4 (not included):_______________",sep="\n")
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Actual Array : ",arr,sep="\n")
print("From the second element, slice elements from index 1 to index 4 (not included)\narr[1,1:4]:\n",arr[1,1:4])

print("_______________From both elements, return index 2:_______________",sep="\n")
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Actual Array : ",arr,sep="\n")
print("FFrom both elements, return index 2:\narr[0:2,2]:\n",arr[0:2,2])



print("_______________From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:_______________",sep="\n")
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Actual Array : ",arr,sep="\n")
print("From both elements, slice index 1 to index 4 (not included), this will return a 2-D array::\n",arr[0:2,1:4])


