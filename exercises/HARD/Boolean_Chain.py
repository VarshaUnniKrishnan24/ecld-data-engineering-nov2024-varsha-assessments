'''Boolean Chain
Write three functions:

boolean_and
boolean_or
boolean_xor
These functions should evaluate a list of True and False values, 
starting from the leftmost element and evaluating pairwise.'''

def boolean_and(lst):
 for i in range(1,len(lst)):
	  lst[i]=lst[i-1] & lst[i]
 return lst[-1]	

def boolean_or(lst):
 for i in range(1,len(lst)):
	  lst[i]=lst[i-1] | lst[i]
 return lst[-1]

def boolean_xor(lst):
 for i in range(1,len(lst)):
	  lst[i]=lst[i-1] ^ lst[i]
 return lst[-1]
	
print(boolean_and([True, True, False, True])) # False 
print(boolean_or([True, True, False, False])) # True 
print(boolean_xor([True, True, False, False])) # False