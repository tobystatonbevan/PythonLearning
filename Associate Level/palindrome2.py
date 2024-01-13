text = input("Enter a word: ")
palindrome = False

if not text.isspace():
    text = text.lower().replace(' ','')
    for i in range(len(text)):
        inverse = (i+1)*-1
        if text[i] == text[inverse]:
            palindrome = True
        else:
            palindrome = False
            break

if palindrome:
    print("It's a palindrome")
else: 
    print("It's not a palindrome")