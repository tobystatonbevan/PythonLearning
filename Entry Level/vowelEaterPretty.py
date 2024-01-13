word_without_vowels = ""
user_word = input("Give me a word: ")
user_word = user_word.upper()
for i in user_word:
    if i == "A":
        continue
    elif i == "E":
        continue
    elif i == "I":
        continue
    elif i == "O":
        continue
    elif i == "U":
        continue
    else:
        word_without_vowels += i
print(word_without_vowels)