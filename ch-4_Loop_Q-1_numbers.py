# Program to print all numbers divisible by 3 between 1 and 1000

# Start at 1
number = 1

# While loop to go through the numbers from 1 to 1000
while number <= 1000:
    # Check if the number is divisible by 3
    if number % 3 == 0:
        print(number)
    # Increment the number
    number += 1
