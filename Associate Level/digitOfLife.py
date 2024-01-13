dob = input("Enter your date of birth in the format YYYYMMDD: ")

while len(dob) != 8 or not dob.isnumeric():
    dob = input("Enter your date of birth in the format YYYYMMDD: ")

sum = 0
doubleDigit = True

for i in dob:
    x = int(i)
    sum += x

if sum <= 9:
   doubleDigit = False

while doubleDigit:
   p = str(sum)
   sum = 0
   for i in p:
      n = int(i)
      sum += n
   if sum <= 9:
      doubleDigit = False

print(sum)