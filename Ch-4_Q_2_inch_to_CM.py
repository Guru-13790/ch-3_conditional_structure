# Inches to Centimeters Converter Program

# Conversion factor: 1 inch = 2.54 cm
INCH_TO_CM = 2.54

# Start the while loop
while True:
    # Ask the user to input the number of inches
    inches = float(input("Enter inches (negative value to stop): "))

    # Check if the input is negative
    if inches < 0:
        print("Program terminated.")
        break

    # Convert inches to centimeters
    centimeters = inches * INCH_TO_CM

    # Print the result
    print(f"{inches} inches is {centimeters:.2f} centimeters.")
