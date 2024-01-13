steps = 0
c0 = int(input("Enter a number: "))

if c0:
    if c0 < 0:
        exit
else:
    exit

while c0 != 1:
    #returns false if odd number
    if c0%2:
        c0 = 3*c0+1
    else:
        c0 /= 2
    print(int(c0))
    steps += 1
print(f"Steps = {steps}")
