'''Number Split
Given a number, return a list containing the two halves of the number. If the number is odd, make the rightmost number higher.'''

import math
def number_split(n):
 lst=[math.floor(n/2),math.ceil(n/2)] #or half1 = n // 2 , half2 = n - half1
 return lst
	

print(number_split(4)) # [2, 2] 
print(number_split(10)) # [5, 5] 
print(number_split(11)) # [5, 6] 
print(number_split(-9)) # [-5, -4]