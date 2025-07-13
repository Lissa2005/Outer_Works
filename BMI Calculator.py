#BMI Calculator

# Get user inputs
weight = float(input("Enter your weight in kilograms: "))
height_in = float(input("Enter your height in inches: "))

# Convert height from inches to meters
height_m = height_in * 0.0254

# Calculate BMI
bmi = weight / (height_m ** 2)

# Display the result
print("Your BMI is:", bmi)

# Provide interpretation
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
