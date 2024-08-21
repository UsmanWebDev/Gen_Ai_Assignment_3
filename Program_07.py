# calculates a percentage

# Get the number and percentage from the user
number = float(input("Enter the number: "))
percentage = float(input("Enter the percentage (%): "))

# Calculate the percentage
result = (number * percentage) / 100

# Print the result
print(f"{percentage}% of {number} is {result}")
