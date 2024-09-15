# Program to check if the zander meets the size limit

# Define the minimum size limit for a zander
size_limit = 42

# Ask the user to input the length of the zander
length = float(input("Enter the length of the zander in centimeters: "))

# Check if the zander meets the size limit
if length >= size_limit:
    print("The zander meets the size limit. You can keep it.")
else:
    # Calculate how many centimeters the fish is below the limit
    shortfall = size_limit - length
    print(f"The zander is too small and should be released back into the lake.")
    print(f"It is {shortfall:.2f} cm below the size limit.")
