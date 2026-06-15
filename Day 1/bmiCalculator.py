
#BMI CALCULATOR
 
# BMI = weight / (height ** 2)

weight =float( input("Enter Your Weight : "))
height = float(input("Enter Your Height (meter ): "))

bmi = weight / (height ** 2)
if bmi < 18.5:
    status = "Underweight"
elif bmi < 25:
    status = "Normal"
elif bmi < 30:
    status = "Overweight"
else:
    status = "Obese"
print (f"Your Bmi Is : {bmi:.2f} and your current status is {status}")
