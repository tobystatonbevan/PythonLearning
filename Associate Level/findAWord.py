textOne = input("Enter string to find: ").lower()
textTwo = input("Enter strong to search: ").lower()
found = False

for i in textOne:
    if i in textTwo:
        found = True
    else:
        found = False
        break

print(found)