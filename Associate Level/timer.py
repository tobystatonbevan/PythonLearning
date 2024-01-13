class Timer:
    def __init__(self, hours = 00, minutes = 00, seconds = 00):
        self.__hr = hours
        self.__mn = minutes
        self.__sc = seconds

    def __str__(self):
        return formatter(self.__hr)+":"+formatter(self.__mn)+":"+formatter(self.__sc)

    def next_second(self):
        self.__sc += 1
        if self.__sc == 60:
            self.__mn += 1
            self.__sc = 0
            if self.__mn == 60:
                self.__hr += 1
                self.__mn = 0
                if self.__hr == 24:
                    self.__hr = 0

    def prev_second(self):
        self.__sc -= 1
        if self.__sc == -1:
            self.__mn -= 1
            self.__sc = 59
            if self.__mn == -1:
                self.__hr -= 1
                self.__mn = 59
                if self.__hr == -1:
                    self.__hr = 23

def formatter(time):
    stringTime = str(time)
    if len(stringTime) == 1:
        stringTime = "0" + stringTime
    return stringTime

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
    