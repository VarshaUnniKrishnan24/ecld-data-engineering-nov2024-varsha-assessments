# Matrix Subtraction
# Two matrices must have an equal number of rows and 
# columns to be subtracted. In which case, the subtracted of two
#  matrices A and B will be a matrix which has the same number of 
# rows and columns as A and B.

# The result of the subtraction of A and B, denoted A - B is computed 
# by subtracting corresponding elements of A and B.

# Create a function that takes 2 x 2D lists lst1 and lst2 as an 
# argument and returns a 2D list (matrix C). C = A-B.


def subtract_matrix(lst1, lst2):
    if len(lst1) != len(lst2) or any(len(row1) != len(row2) for row1, row2 in zip(lst1, lst2)):
        raise ValueError("Matrices must have the same number of rows and columns.")
    
    result = []
    for i in range(len(lst1)):
        row = []
        for j in range(len(lst1[0])):
            row.append(float(lst1[i][j]) - float(lst2[i][j]))
        result.append(row)
    return result

				
print(subtract_matrix([ ['1', '2', '3'], 
['4', '5', '6'],
['7', '8', '9'] ],
[ ['1', '2', '3'], 
['4', '5', '6'],
['7', '8', '9'] ])) # Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
	 