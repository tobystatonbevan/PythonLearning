def is_year_leap(year):

    if year < 1582:
        print("Not within the Gregorian calendar period")
        return None
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

def days_in_month(year, month):
    if year < 1582 or month not in range(1,13):
        return None
    daysInMonths = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_year_leap(year):
        daysInMonths[1] = 29
    return daysInMonths[month-1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")