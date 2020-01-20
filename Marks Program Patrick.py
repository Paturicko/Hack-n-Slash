#Author: Patrick
#MARKS PROGRAM

#Input Marks
mark1 = int(input("Enter math mark"))
mark2 = int(input("Enter english mark"))
mark3 = int(input("Enter science mark"))
mark4 = int(input("Enter history mark"))

#Calculate Average
avg = (mark1 + mark2 + mark3 + mark4)/4
print("Overall Average:", avg)

#Print Letter Grade
if (avg >= 80):
    print("A, great work.")
elif (avg >= 70):
    print("B, good job.")
elif (avg >= 60):
    print("C, ok job.")
elif (avg >= 50):
    print("D, try harder.")
else:
    print("F, oh no.")

