import calendar

class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self,yr,wkd):
        cal = []
        counter = 0
        for i in range(1,13):
            fullYear = self.monthdays2calendar(yr,i)
            for n in fullYear:
                for p in n:
                    cal.append(p)
        for t in cal:
            if t[0] != 0 and t[1] == wkd:
                counter += 1
        return counter
    
print(MyCalendar().count_weekday_in_year(2000,6))