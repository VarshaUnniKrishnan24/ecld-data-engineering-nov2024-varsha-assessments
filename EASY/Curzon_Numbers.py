# Curzon Numbers
# In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.

# Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.

def is_curzon(num):
	numerator = 2 ** num + 1
	denominator = 2 * num + 1
	return numerator % denominator == 0
	
print(is_curzon(5)) # True 
print(is_curzon(10)) # False 
print(is_curzon(14)) # True