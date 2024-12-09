

# Basic Arithmetic Operations on a String Number
# Create a function to perform basic arithmetic operations that 
# includes addition, subtraction, multiplication and division on a 
# string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

# Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.

# eval() is not allowed. In case of division, whenever the second number equals "0" return -1.



def arithmetic_operation(n):
    try:
        a, op, b = n.split()
        
        a = int(a)
        b = int(b)
        
        switch = {
            '+': a + b,
            '-': a - b,
            '*': a * b,
            '//': a // b if b != 0 else -1
        }
        
        result = switch.get(op)
        if result is None:
            return "Invalid operator"
        return result
    
    except ValueError:
        return "Invalid format. Required format: 'number operator number"
    

print(arithmetic_operation("12 + 12")) # 24 
print(arithmetic_operation("12 - 12")) # 0 
print(arithmetic_operation("12 * 12")) # 144 
print(arithmetic_operation("12 // 0")) # -1
print(arithmetic_operation("12 // 3"))  # 4
print(arithmetic_operation("12 & 12"))  # Invalid operator
print(arithmetic_operation("12 + abc"))  # Invalid format. Required format: 'number operator number
print(arithmetic_operation("12"))  # Invalid format. Required format: 'number operator number






# def arithmetic_operation(n):
#     a, op, b = n.split()
#     a = int(a)
#     b = int(b)
    
#     if op == '+':
#         return a + b
#     elif op == '-':
#         return a - b
#     elif op == '*':
#         return a * b
#     elif op == '//':
#         if b == 0:
#             return -1
#         else:
#             return a // b
#     else:
#         return None

# # Test examples
# print(arithmetic_operation("12 + 12"))  # 24
# print(arithmetic_operation("12 - 12"))  # 0
# print(arithmetic_operation("12 * 12"))  # 144
# print(arithmetic_operation("12 // 0"))  # -1
# print(arithmetic_operation("12 // 3"))  # 4
