''' Perfect Square Patch
Create a function that takes an integer and outputs an n x n square solely consisting of the integer n.'''

def square_patch(n):
 matrix = [[n]*n for i in range(n)]
 return matrix
	
print(square_patch(3)) # ➞ [ # [3, 3, 3], # [3, 3, 3], # [3, 3, 3] # ] 
print(square_patch(5)) # ➞ [ # [5, 5, 5, 5, 5], # [5, 5, 5, 5, 5], # [5, 5, 5, 5, 5], # [5, 5, 5, 5, 5], # [5, 5, 5, 5, 5] # ] 
print(square_patch(1)) # ➞ [ # [1] # ] 
print(square_patch(0)) # ➞ []