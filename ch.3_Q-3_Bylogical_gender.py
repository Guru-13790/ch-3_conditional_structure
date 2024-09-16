# Hemoglobin Level Checker Program

# Ask the user for their biological gender
gender = input("Enter your biological gender (male/female): ").lower()

# Ask for the hemoglobin value
hemoglobin_value = float(input("Enter your hemoglobin value (g/l): "))

# Check the hemoglobin levels based on the user's gender
if gender == "female":
    if hemoglobin_value < 117:
        print("Your hemoglobin value is low.")
    elif 117 <= hemoglobin_value <= 155:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
elif gender == "male":
    if hemoglobin_value < 134:
        print("Your hemoglobin value is low.")
    elif 134 <= hemoglobin_value <= 167:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
else:
    print("Invalid gender input. Please enter 'male' or 'female'.")
