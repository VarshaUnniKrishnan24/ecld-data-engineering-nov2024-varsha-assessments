# Calculating Damage
# Create a function that takes damage and speed (attacks per second) and returns the amount of damage after a given time.


def damage(damage, speed, time):
 if damage<0 or speed<0 :
	  return "invalid"
 else:
	  if time=='second':
	    return damage*speed*1
	  elif time=='minute':
	    return damage*speed*60
	  elif time=='hour':
	    return damage*speed*3600
	  else:
	    return "invalid"
	
print(damage(40, 5, "second")) # 200 
print(damage(100, 1, "minute")) # 6000 
print(damage(2, 100, "hour")) # 720000 
print(damage(-2, 100, "hour")) # "invalid"