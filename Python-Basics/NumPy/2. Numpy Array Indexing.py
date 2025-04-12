import numpy as np


"""
dtype as string
"""
print("_______________dtype as string_______________")
arr = np.array([1,2,3],dtype=str)
print("Actual : ", arr)
print(" arr[0]: ",arr[0])
print(" arr[1]: ",arr[1])

print(" arr[1]+arr[2]: ",arr[1]+arr[2])            # will print 23 , because dtype=str


"""
dtype as int
"""
print("_______________dtype as int_______________")
arr = np.array([1,2,3],dtype=int)
print("Actual : ", arr)
print(" arr[0]: ",arr[0])
print(" arr[1]: ",arr[1])
print(" arr[2]: ",arr[2])
print(" arr[1]+arr[2]: ",arr[1]+arr[2])            # will print 5 , because dtype=int



print("_______________Indexing Of 2d Array_______________")
arr = np.array(([1,2,3],[4,5,6]),dtype=str)
print("Actual : ", arr,sep='\n')

print(" arr[0]: ",arr[0])       
print(" arr[1]: ",arr[1])

print(" arr[0,0]: ",arr[0,0])       
print(" arr[0,1]: ",arr[0,1])
print(" arr[0,2]: ",arr[0,2])

print(" arr[1,0]: ",arr[1,0])       
print(" arr[1,1]: ",arr[1,1])
print(" arr[1,2]: ",arr[1,2])

print("_______________Accessing Arra From End_______________")
arr = np.array(([1,2,3],[4,5,6]),dtype=str)
print("Actual : ", arr,sep='\n')
print("arr[-1]: ",arr[-1])       
print("arr[-2]: ",arr[-2])

print("arr[-1,-1]: ",arr[-1,-1])       
print("arr[-1,-2]: ",arr[-1,-2])  
print("arr[-1,-3]: ",arr[-1,-3])  

print("arr[-2,-1]: ",arr[-2,-1])       
print("arr[-2,-2]: ",arr[-2,-2])  
print("arr[-2,-3]: ",arr[-2,-3])  
