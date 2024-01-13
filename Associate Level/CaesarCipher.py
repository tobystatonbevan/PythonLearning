text = input("Enter your message: ")
displacement = ''
while type(displacement) != int:
    try:
        displacement = int(input("Enter shift value: "))
        if displacement < 1 or displacement > 25:
            displacement = ''
    except: 
        continue

cipher = ''
for char in text:
    lowercase = False
    if not char.isalpha():
        cipher += char
        continue
    if char.islower():
     char = char.upper()
     lowercase = True
    code = ord(char) + displacement
    if code > ord('Z'):
        code -= 26
    if lowercase:
        cipher += chr(code).lower()
    else:
        cipher += chr(code)

print(cipher)