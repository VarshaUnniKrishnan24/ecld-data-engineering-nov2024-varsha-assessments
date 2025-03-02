# FizzBuzz Interview Question
# Create a function that takes a number as an argument and returns 
# "Fizz", "Buzz" or "FizzBuzz".

# If the number is a multiple of 3 the output should be "Fizz".
# If the number given is a multiple of 5, the output should be "Buzz".
# If the number given is a multiple of both 3 and 5, the output should
#  be "FizzBuzz".
# If the number is not a multiple of either 3 or 5, the number should
#  be output on its own as shown in the examples below.
# The output should always be a string even if it is not a multiple 
# of 3 or 5.

def fizz_buzz(num):
    if not isinstance(num, int):  
        return "Invalid input"
    
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)
	  
print(fizz_buzz(3)) # "Fizz" 
print(fizz_buzz(5)) # "Buzz" 
print(fizz_buzz(15)) # "FizzBuzz" 
print(fizz_buzz(4)) # "4"