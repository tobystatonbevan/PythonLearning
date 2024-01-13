from datetime import datetime

obj = datetime(2020,11,4,14,53,00)

print(obj.strftime("%Y/%m/%d %H:%M:%S"))
print(obj.strftime("%y/%B/%d %H:%M:%S %p"))
print(obj.strftime("%a, %Y %b %d"))
print(obj.strftime("Weekday: %w"))
print(obj.strftime("Day of the year: %j"))
print(obj.strftime("Week number of the year: %W"))