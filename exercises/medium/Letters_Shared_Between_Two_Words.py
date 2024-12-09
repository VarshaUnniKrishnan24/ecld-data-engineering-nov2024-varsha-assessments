''' Letters Shared Between Two Words
Create a function that returns the number of characters shared between two words.'''


def shared_letters(txt1, txt2):
 lst=list(set(txt1)&set(txt2))
 return len(lst)
	
print(shared_letters("apple", "meaty")) # 2 
print(shared_letters("fan", "forsook")) # 1 
print(shared_letters("spout", "shout")) # 4