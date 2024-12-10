# Sum of Odd and Even Numbers
# Write a function that takes a list of numbers and returns 
# a list with two elements:

# The first element should be the sum of all even numbers in the list.
# The second element should be the sum of all odd numbers in the list.

def sum_odd_and_even(lst):
    if not isinstance(lst, list) or not all(isinstance(i, int) for i in lst):
        return "Invalid input"
    
    even = sum(e for e in lst if e % 2 == 0)
    odd = sum(e for e in lst if e % 2 != 0)
    
    return [even, odd]

print(sum_odd_and_even([1, 2, 3, 4, 5, 6])) # [12, 9] 
print(sum_odd_and_even([-1, -2, -3, -4, -5, -6])) # [-12, -9] 
print(sum_odd_and_even([0, 0])) # [0, 0]