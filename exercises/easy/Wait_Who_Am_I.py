'''
Wait... Who Am I?
Hello there, I... seem to not remember who I am, my memories is all... cloudy, although maybe if I could piece it together...

Oh! Maybe you could help me make a class that helps me remember things. Maybe a method called add that would add to my memory if I would recall things and a remember method that would let me recall a specific memory.

But you have to make add more flexible, I might recall many things in an instant or only one that I would forget again.

Examples :D
# add method doesn't return anything.
memories.add(name="Shane", gender="M", catch_phrase="bazinga")

memories.add(work="None", love_life=0)

memories.add(adress="car")

memories.remember("work") ➞ "None"

memories.remember("gender") ➞ "M"

# If memory was not added, return False
memories.remember("lover") ➞ False
Notes
The add method should be able to handle any number of arguments.'''

class Memory:
    def __init__(self):
        self.memories = {}
    
    def add(self, **kwargs):
        for key, value in kwargs.items():
            self.memories[key] = value
    
    def remember(self, key):
        return self.memories.get(key, False)

memories = Memory()
memories.add(name="Shane", gender="M", catch_phrase="bazinga")
memories.add(work="None", love_life=0)
memories.add(adress="car")

print(memories.remember("work"))       
print(memories.remember("gender"))     
print(memories.remember("lover"))     
