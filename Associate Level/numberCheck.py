def read_int(prompt, min, max):
    value = -999999

    while value < min or value > max:
        if value != -999999:
            print(f"Error: the value is not within the permitted range ({min}..{max})")
        try:
            value = int(input(prompt))
        except: 
            print("Error: wrong input")
            value = int(input(prompt))
    return value


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
    