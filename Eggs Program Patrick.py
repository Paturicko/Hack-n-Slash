#Author: Patrick
#EGGS PROGRAM

#Input Number of Eggs
eggs = int(input("Enter number of eggs"))

#Calculate Number of Dozen Eggs & Remainder
dozen = int(eggs / 12)
remainder = eggs % 12
print("remainder:",remainder)
print("Dozen of eggs: ",dozen)

#Get Price & Calculate Extra Price
if (dozen >= 11):
    price = 0.35
elif (dozen >= 6):
    price = 0.40
elif (dozen >= 4):
    price = 0.4
else:
    price = 0.5
extra_price = price / 12 * remainder

#Print Total Price
print("The bill is equal to:", price * dozen+extra_price )

