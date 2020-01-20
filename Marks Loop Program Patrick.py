#Author: Patrick
#MARKS LOOP PROGRAM

#Initialize Sum Variable
sum = 0

#Calculate Total Sum
for i in range(1,5):
    mark = int(input("Enter your mark"))
    sum = sum + mark

#Print Total Average
print("TOTAL", sum/4)
