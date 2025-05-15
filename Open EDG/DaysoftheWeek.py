class WeekDayError(Exception):
    pass


class Weeker:
    Days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day not in Weeker.Days:
            raise WeekDayError
        else: self.day = day

    def __str__(self):
        return self.day

    def add_days(self, n):
        i = Weeker.Days.index(self.day)
        m = (i + n) % 7
        self.day = Weeker.Days[m]

    def subtract_days(self, n):
        i = Weeker.Days.index(self.day)
        m = (i - n) % 7
        self.day = Weeker.Days[m]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
