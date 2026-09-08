import numpy as np 


ar = np.array([[1,2,3,4],[12,3,4,5]])

print(ar.ndim) # it tell the dim 2d or 3d 

print(ar.shape)  # it tells the no of row and coloms 

print(ar.dtype) # its a data tyep 

print(ar.size) # it tell the total no of elements


x = np.full((2, 3), 9)  # used to fill elemtn with same value 

print(x)



x = np.eye(3)  # used to create a identy matrix 

print(x)




# Random Numbers 



x =  np.random.rand(5)  #  it produce the randome num btw 0 and 1
print(x)



x = np.random.randn(5)   #Generates random numbers from a standard normal distribution , the value can be negative , postive around zero
print(x)



x = np.random.randint(1, 10, 5) # it produces the random integers whole nums ( start, stop , step)
print(x)




np.random.uniform(10, 20, 5)  # it generate the value in uniform distribution


scores = np.random.normal(70, 10, 100) # it generates the values in normal distribuution



np.random.seed(42)  # it is used for to get teh same random values again and again , it is called reproducablityr , we can control the random sequence




