''' Hashtag Generator
Create a function that is a Hashtag Generator by using the following rules:

The output must start with a hashtag (#).
Each word in the output must have its first letter capitalized.
If the final result, a single string, is longer than 140 characters, the function should return false.
If either the input (str) or the result is an empty string, the function should return false.'''

def generate_hashtag(txt):
    if txt.replace(" ","")== "":
        return False
    else :
        s="#"
        s+=txt.title().replace(" ","")
        return s if len(s) <= 140 else False 
    
print(generate_hashtag(" Hello World ")) # ➞ "#HelloWorld" 
print(generate_hashtag("")) # ➞ False 
print(generate_hashtag("Edabit Is Great")) # ➞ "#EdabitIsGreat"



# def generate_hashtag(txt):
#     # Check if the input is an empty string or only contains spaces
#     if not txt.strip():
#         return False
    
#     # Convert the string to title case and split into words
#     words = txt.title().split()
    
#     # Join words with no spaces and prepend the hashtag
#     hashtag = "#" + "".join(words)
    
#     # Check if the hashtag is longer than 140 characters
#     if len(hashtag) > 140:
#         return False
    
#     return hashtag


