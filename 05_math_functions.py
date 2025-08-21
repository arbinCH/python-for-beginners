x = 3.14
y = -4
z = 5

# result = round(x)      # provides round result, if the value is in decimal number.
# result = abs(y)        # provides the abosolute value in positive, even the number is negative. 
# result = pow(y, 2)       # -4 ** 2 = 16
# result = max(x, y, z)  # provides the maximum value from the given values
# result = min(x, y, z)  # provides the minimum value from the given values

# print(result)


# import math

# print(math.pi)  # provides the value of pi


# import math

# x = 9.9

# result = math.sqrt(x)  # provides the square root of the given value    
# result = math.ceil(x)  # rounds up to the nearest whole number
# result = math.floor(x)  # rounds down to the nearest whole number
# print(result)  


# calculating the circumference of radius.

# import math

# radius = float(input("Enter the radius of the circle: "))    

# circumference = 2 * math.pi * radius
# print(f"The circumference of the circle is:{round(circumference, 2)} cm")  
 

# # calculating area of radius.

# import math

# radius = float(input("Enter the radius of the circle: "))    

# area = math.pi * radius**2
# print(f"The area of the circle is:{round(area, 2)} cm^2")


# calculating the hypotenuse of a right triangle

import math

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))  # Pythagorean theorem

print(f"side c = {c}")