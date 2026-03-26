'''
Part A: Basics & Array Creation
'''
#Q1. Create a NumPy array from a Python list [1, 2, 3, 4, 5]. Print its type and shape.
import numpy as np
python_list = [1, 2, 3, 4, 5]
numpy_array = np.array(python_list)
print("Type:", type(numpy_array))
print("Shape:", numpy_array.shape)

#Q2. Create a 3x3 matrix of zeros and a 3x3 matrix of ones.
zeros_matrix = np.zeros((3, 3))
ones_matrix = np.ones((3, 3))
print("3x3 Zeros Matrix:\n", zeros_matrix)
print("3x3 Ones Matrix:\n", ones_matrix)

#Q3. Generate an array of numbers from 10 to 50 with step size 5.
range_array = np.arange(10, 51, 5)
print("Array from 10 to 50 (step 5):", range_array)

#Q4. Create a 4x4 identity matrix.
identity_matrix = np.eye(4)
print("4x4 Identity Matrix:\n", identity_matrix)

#Q5. Generate a 2x3 array of random numbers between 0 and 1.
random_array = np.random.rand(2, 3)
print("2x3 Random Array:\n", random_array)

'''
Part B Indexing & Slicing (15 mins) [MAIN FOCUS]
'''
#Q1. Given arr = np.array([10, 20, 30, 40, 50]), access the first, last, and third element.
arr = np.array([10, 20, 30, 40, 50])
first_element = arr[0]
last_element = arr[-1]
third_element = arr[2]
print("First element:", first_element)
print("Last element:", last_element)
print("Third element:", third_element)


#Q2. Create a 4x4 matrix and extract:
#a) First row
#b) Last column
#c) Middle 2x2 submatrix

matrix = np.random.rand(4, 4)
first_row = matrix[0]
last_column = matrix[:, -1]
middle_submatrix = matrix[1:3, 1:3]
print("4x4 Matrix:\n", matrix)
print("First row:\n", first_row)
print("Last column:\n", last_column)
print("Middle 2x2 submatrix:\n", middle_submatrix)

#Q3. Given arr = np.arange(1, 11), slice elements from index 2 to 7.

arr = np.arange(1, 11)
sliced_arr = arr[2:8]   
print("Sliced array (index 2 to 7):", sliced_arr)

#Q4. Modify elements at even indices to zero in an array.
arr = np.arange(1, 11)
arr[::2] = 0    
print("Array after modifying even indices to zero:", arr)

#Q5. Given a 5x5 matrix, extract all elements greater than 10 using boolean indexing.
matrix = np.random.randint(1, 20, (5, 5))
greater_than_10 = matrix[matrix > 10]
print("5x5 Matrix:\n", matrix)
print("Elements greater than 10:", greater_than_10)

#Q6. Replace all negative values in an array with 0.
arr = np.array([-1, 2, -3, 4, -5])
arr[arr < 0] = 0
print("Array after replacing negative values with 0:", arr)

#Q7. Given a matrix, reverse rows and columns using slicing.
matrix = np.random.rand(4, 4)
reversed_matrix = matrix[::-1, ::-1]
print("Original Matrix:\n", matrix)
print("Reversed Matrix:\n", reversed_matrix)


#Q8. Extract diagonal elements of a matrix.
matrix = np.random.rand(4, 4)
diagonal_elements = np.diag(matrix)
print("Matrix:\n", matrix)
print("Diagonal elements:", diagonal_elements)

'''
Part C: Broadcasting & Shape Manipulation (10 mins)
'''
#Q1. Add a scalar value of 5 to each element in an array.
arr = np.array([1, 2, 3, 4, 5])
arr += 5
print("Array after adding 5:", arr)

#Q2. Add two arrays of different shapes using broadcasting.
arr1 = np.array([1, 2, 3])
arr2 = np.array([[10], [20], [30]])
result = arr1 + arr2
print("Result of using broadcasting:\n", result)   

#Q3. Multiply a 3x3 matrix with a 1D array using broadcasting.
matrix = np.random.rand(3, 3)
array = np.array([1, 2, 3])
result = matrix * array
print("3x3 Matrix:\n", matrix)
print("1D Array:", array)
print("Result of multiplication using broadcasting:\n", result)

#Q4. Reshape a 1D array of size 12 into (3,4) and (2,6).
arr = np.arange(12)
reshaped_3_4 = arr.reshape(3, 4)
reshaped_2_6 = arr.reshape(2, 6)
print("Original array:", arr)
print("Reshaped to (3,4):\n", reshaped_3_4)
print("Reshaped to (2,6):\n", reshaped_2_6)

#Q5. Flatten a 2D array into 1D.
matrix = np.random.rand(3, 3)
flattened_array = matrix.flatten()
print("Original 2D array:\n", matrix)
print("Flattened 1D array:", flattened_array)


#Q6. Transpose a 3x2 matrix.
matrix = np.random.rand(3, 2)
transposed_matrix = matrix.T
print("Original 3x2 matrix:\n", matrix)
print("Transposed 2x3 matrix:\n", transposed_matrix)

#Q7. Stack two arrays vertically and horizontally.
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
vertical_stack = np.vstack((arr1, arr2))
horizontal_stack = np.hstack((arr1, arr2))
print("Vertical Stack:\n", vertical_stack)
print("Horizontal Stack:\n", horizontal_stack)


#Q8. Expand dimensions of a 1D array into 2D using reshape.
arr = np.array([1, 2, 3, 4])
expanded_array = arr.reshape(4, 1)
print("Original 1D array:", arr)
print("Expanded 2D array:\n", expanded_array)


'''
Part D: Mathematical Functions 
'''

#Q1. Find mean, median, and standard deviation of an array.
arr = np.array([1, 2, 3, 4, 5])
mean = np.mean(arr)
median = np.median(arr)
std_dev = np.std(arr)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

#Q2. Compute element-wise square and square root of an array.
arr = np.array([1, 4, 9, 16, 25])
squared = np.square(arr)
square_root = np.sqrt(arr)
print("Original array:", arr)
print("Squared array:", squared)
print("Square root array:", square_root)

#Q3. Find min and max values along rows and columns of a matrix.
matrix = np.random.rand(3, 3)
min_along_rows = np.min(matrix, axis=1)
max_along_columns = np.max(matrix, axis=0)
print("Matrix:\n", matrix)
print("Min values along rows:", min_along_rows)
print("Max values along columns:", max_along_columns)


#Q4. Perform element-wise addition, subtraction, multiplication, and division of two arrays.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
addition = arr1 + arr2
subtraction = arr1 - arr2
multiplication = arr1 * arr2
division = arr1 / arr2
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
        