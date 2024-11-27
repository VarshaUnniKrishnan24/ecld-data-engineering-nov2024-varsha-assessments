# A Circle and Two Squares
# Imagine a circle and two squares: a smaller and a bigger one. 
# For the smaller one, the circle is a circumcircle and for the 
# bigger one, an incircle.


# 1. Bigger Square (Incircle):
#    - Side length = diameter of the circle =  2r 
#    - Area =  (2r)^2 = 4r^2 

# 2. Smaller Square Circumcircle:
#    - Diagonal = diameter of the circle =  2r 
#    - Side length =  \frac{2r}{\sqrt{2}} = r\sqrt{2} 
#    - Area =  (r\sqrt{2})^2 = 2r^2 

# 3. Difference of Areas**:
#    4r^2 - 2r^2 = 2r^2 

# So, the difference in areas is  2r^2  

def square_areas_difference(r):
    if not isinstance(r, (int, float)) or r < 0:  
        return "Invalid input"
    return (2*r)**2 - 2*(r**2)


print(square_areas_difference(5)) # 50 
print(square_areas_difference(6)) # 72 
print(square_areas_difference(7)) # 98