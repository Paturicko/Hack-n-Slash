#Author: Patrick
#PAYROLL PROGRAM

#Input Name, Wage & Hours
name = input("What's your name?")
wage = float(input("Enter your hourly wage"))
hours = float(input("Enter hours"))

#Calculate Grosspay & Netpay
pay = wage*hours
tax = pay * .1
netpay = pay - tax

#Print Grosspay & Netpay
print("Your grosspay is", pay)
print("Your netpay is", netpay)

