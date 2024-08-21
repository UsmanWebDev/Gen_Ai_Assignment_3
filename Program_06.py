# converts a given number of seconds into minutes and seconds:

# Get the number of seconds from the user
total_seconds = int(input("Enter the total number of seconds: "))

# Calculate the minutes and seconds
minutes = total_seconds // 60
seconds = total_seconds % 60

# Print the result
print(f"{total_seconds} seconds is equal to {
      minutes} minutes and {seconds} seconds")
