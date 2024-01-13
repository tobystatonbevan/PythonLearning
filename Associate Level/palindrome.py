text = input("Enter a word: ")
palindrome = False

if not text.isspace():
    text = text.lower().replace(' ','')
    if text == text[::-1]:
        palindrome = True

if palindrome:
    print("It's a palindrome")
else: 
    print("It's not a palindrome")