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


# Ex 1

arr = np.array([10, 20, 30, 40, 50, 60, 70])
"""
The first element
The last element
The 4th element
The 2nd-last element
"""

print(arr[0])
print(arr[-1])
print(arr[3])

print(arr[-2])
print()

# ex 2
arr1 = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

"""
[10, 15, 20, 25]
[30, 35, 40, 45, 50]
Every second element
Every third element

"""

print(arr1[1:5])
print(arr1[5:])
print(arr1[::2])
print(arr1[::3])
print()

# Ex 3

reverse = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(reverse[::-1])

print()


# ex 4
"""
array[row,col]

"""

arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr2[1,1])

print(arr2[0,2])

print(arr2[2,0])

print(arr2[2,1])

print()

# ex 5

arr3 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])


print(arr3[0])
print(arr3[-1])

print(arr3[0:2])

print(arr3[2:])

print()

#EX 5

arr4 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print(arr4[:,0])
print(arr4[:,-1])
print(arr4[:,1])
print(arr4[:,0:2])

print()

# Ex 6

arr6 = np.array([
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])


print(arr6[1:4,1:4])

print()

# ex 8 

arr7 = np.arange(1, 26).reshape(5, 5)
print(arr7)

print()

print(arr7[0,0::2])
print(arr7[2,0::2])
print(arr7[4,0::2])

print()


# ex 9

arr = np.arange(1, 11)

print(arr)

arr[:4] = 100
arr[8:] = 500
arr[::2] = 0
print()
print(arr)



data = np.array([
    [21, 50000, 2],
    [25, 60000, 3],
    [30, 75000, 5],
    [35, 90000, 4],
    [40, 120000, 6]
])

# Columns:
# Age | Salary | Experience


# 1. Extract all ages
ages = data[:, 0]
print("1. All ages:")
print(ages)


# 2. Extract all salaries
salaries = data[:, 1]
print("\n2. All salaries:")
print(salaries)


# 3. Extract all experience values
experience = data[:, 2]
print("\n3. All experience values:")
print(experience)


# 4. Extract the first 3 rows
first_3_rows = data[:3]
print("\n4. First 3 rows:")
print(first_3_rows)


# 5. Extract the last 2 rows
last_2_rows = data[-2:]
print("\n5. Last 2 rows:")
print(last_2_rows)


# 6. Extract age + salary for every person
age_salary = data[:, :2]
print("\n6. Age + Salary:")
print(age_salary)


# 7. Extract salary + experience for the last 3 people
salary_experience = data[-3:, 1:]
print("\n7. Salary + Experience for last 3 people:")
print(salary_experience)


# 8. Extract the middle 3 people and only their salary
middle_3_salary = data[1:4, 1]
print("\n8. Salary of middle 3 people:")
print(middle_3_salary)



