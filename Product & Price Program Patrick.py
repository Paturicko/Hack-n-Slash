#Author: Patrick
#PRODUCT & PRICE PROGRAM

#Input Name & Price
product = input("Enter in your product name ")
price=float(input("How much does a "+product+" cost? "))


#Calculate & Print Total Cost
total = price * 1.13
print("The total cost of a", product,"including HST will be:",total)