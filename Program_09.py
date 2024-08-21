# calculates the volume of a cylinder

# Import the math module for the value of pi
import math

# Get the radius and height from the user
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Calculate the volume using the formula: volume = pi * r^2 * h
volume = math.pi * (radius ** 2) * height

# Print the volume
print("The volume of the cylinder is: ", round(volume, 2))
