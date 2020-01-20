#Author: Patrick
#PACKAGE CHECK PROGRAM

#Input Dimensions & Weight
length = int(input("Enter length in cm"))
width = int(input("Enter width in cm"))
height = int(input("Enter height in cm"))
weight = int(input("Enter weight in kg"))

#Print Requirement Message
if (length * width * height > 100000 & weight > 28):
    print("Too heavy and too large")
elif (length * width * height > 100000):
    print("Too large")
elif (weight > 28):
    print("Too heavy")
else:
    print("Meets weight and size requirements")




