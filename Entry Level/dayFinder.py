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


def day_of_year(year, month, day):
    daysOfWeek = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    daysElapsed= 0

    for i in range(1804, year):
        #print(i)
        for p in range(1,13):
            #print(p)
            daysElapsed += days_in_month(i, p)
            #print(daysElapsed)
    for n in range(1, month):
        daysElapsed += days_in_month(year, n)
        #print(n)
    daysElapsed += day-1
    #+1 for index offset
    return daysOfWeek[(daysElapsed)%7]

print(day_of_year(2000, 12, 31))

test_data = [[1900, 10, 11], [2000,1,13], [2016,7,29], [1987,3,3]]
test_results = ["Thursday", "Thursday", "Friday", "Tuesday"]
for i in range(len(test_data)):
    yr,mnth,dy = test_data[i][0], test_data[i][1], test_data[i][2]
    print(yr,"->",end="")
    result = day_of_year(yr,mnth,dy)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")