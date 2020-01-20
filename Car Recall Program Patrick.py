#Author: Patrick
#CAR RECALL PROGRAM

#Input Model Number
model = int(input("Enter car model number"))

#Print Result
if (model >= 189 and model <= 195):
    print("Your car is defective. It must be repaired")
elif (model == 179 or model == 221 or model == 119 or model == 780):
    print("Your car is defective. It must be repaired")
else:
    print("Your car is not defective.")