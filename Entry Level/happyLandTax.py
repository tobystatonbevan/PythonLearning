income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
elif income >= 85528:
	tax = 14839.02 + (income-85528)*0.32

if tax < 0:
	tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
 