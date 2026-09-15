import numpy as np



arr = np.array([[1,2,3,4],
               [2,3,45,7]])


print(arr.shape) # it tells row /coloum

print(arr.size) # it tells no of elements in the array

print(arr.ndim)  # it tells the dimension of it



# AXIS

#  axis tells NumPy which dimension to perform an operation on.
"""

axis 0 = |down 

axis 1 = ->across

"""


arr = np.array([

    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])


print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))
print(np.sum(arr))


print()


arr = np.array([
    [12, 45, 23, 18],
    [56, 34, 78, 21],
    [31, 67, 15, 89]
])

#Maximum value from each column
print(np.max(arr[:,0],axis=0))
print(np.max(arr[:,1],axis=0))
print(np.max(arr[:,2],axis=0))
print(np.max(arr[:,3],axis=0))


#Maximum value from each row
print(np.max(arr[0],axis=0))
print(np.max(arr[1],axis=0))
print(np.max(arr[2],axis=0))


# Minimum value from each column
print(np.min(arr[:,0],axis=0))
print(np.min(arr[:,1],axis=0))
print(np.min(arr[:,2],axis=0))
print(np.min(arr[:,3],axis=0))


#Minimum value from each row 
print(np.min(arr[0],axis=0))
print(np.min(arr[1],axis=0))
print(np.min(arr[2],axis=0))

"""
np.min()    # → What is the smallest value?
np.argmin() # → Where is the smallest value?

np.max()    # → What is the biggest value?
np.argmax() # → Where is the biggest value?

"""


"""
important

"""

x = np.array([10, 20, 30, 40])

wh =np.where( x>20 , 1,0)

print(wh)


# broadcasting

#Broadcasting allows NumPy to perform operations between arrays of different shapes.
# NumPy tries to automatically adjust the smaller array so that the operation can happen.

prices = np.array([
    [100, 200, 300],
    [400, 500, 600]
])

tax = np.array([10, 20, 30])

prices + tax






