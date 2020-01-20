#Author: Patrick
#PRICE PRINTING PROGRAM

#Input Number of Copies
copies = int(input("Enter number of copies"))

#Calculate Price / Copy
if (copies > 1000):
    price = 0.25
elif (copies >= 750):
    price = 0.26
elif (copies >= 500):
    price = 0.27
elif (copies >= 100):
    price = 0.28
else:
    price = 0.3

#Print Price
print("Price per copy is:", price)
print("Total cost is:", copies * price)

