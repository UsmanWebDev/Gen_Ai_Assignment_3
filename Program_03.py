# calculates the area of a circle


import math

radius = float(input("Enter the radius of the circle: "))

# formula: area = pi * r^2
area = math.pi * (radius ** 2)

# Print the area
print("The area of the circle is:", area)
