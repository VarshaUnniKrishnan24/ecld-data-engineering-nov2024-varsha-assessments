# Get Students with Names and Top Notes
# Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a dictionary of objects like { "name": "John", "top_note": 5 }.

def top_note(student):
 new_dictionary = {"name": student["name"], "top_note": max(student["notes"])}
 return new_dictionary
	
print(top_note({ "name": "John", "notes": [3, 5, 4] })) # { "name": "John", "top_note": 5 } 
print(top_note({ "name": "Max", "notes": [1, 4, 6] })) # { "name": "Max", "top_note": 6 } 
print(top_note({ "name": "Zygmund", "notes": [1, 2, 3] }))  # { "name": "Zygmund", "top_note": 3 }