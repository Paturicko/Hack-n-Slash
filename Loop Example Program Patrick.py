#Author: Patrick
#LOOP EXAMPLE PROGRAM

#Initialize Amount Variable
amount = 0.01

#Calculate & Print Amount Per Day
for i in range(1,31):
    amount = amount * 2
    print("Sept", i, amount)
