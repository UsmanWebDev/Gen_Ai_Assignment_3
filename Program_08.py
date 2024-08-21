# calculates the BMI (Body Mass Index):

# Get the height and weight from the user
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate the BMI
bmi = weight / (height ** 2)

# Print the BMI
print("Your BMI is: ", round(bmi, 2))


if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are normal weight")
elif bmi < 30:
    print("You are overweight")
else:
    print("You are obese")
