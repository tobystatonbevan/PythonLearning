def is_year_leap(year):

    if year < 1582:
        print("Not within the Gregorian calendar period")
        return False
    else:
        if year % 4 != 0:
            #print(str(year)+"first condition")
            return False
        elif year % 100 != 0:
            #print(str(year)+"second condition")
            return True
        elif year % 400 != 0:
            #print(str(year)+"third condition")
            return False
        else: 
            #print(str(year)+"fourth condition")
            return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")