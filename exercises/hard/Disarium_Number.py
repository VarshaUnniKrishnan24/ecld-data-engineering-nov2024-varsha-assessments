# Disarium Number
# A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.

# Create a function that determines whether a number is a Disarium or not.


def is_disarium(n):
    if not isinstance(n, int) or n <= 0:
        return "Please input a positive integer."
    ans = 0
    for position, item in enumerate(str(n), 1):
        ans += int(item) ** position
    return ans == n


# str_num = str(number) 
# length = len(str_num) 
# total = sum(int(str_num[i]) ** (i + 1) for i in range(length))
# return total == number

print(is_disarium(75))    # False
print(is_disarium(135))   # True
print(is_disarium(544))   # False
print(is_disarium(518))   # True
print(is_disarium(466))   # False
print(is_disarium(8))     # True
