def clock(h,m,s):
    h = str(h)
    m = str(m)
    s = str(s)
    if len(h) != 2:
        h = "0"+ h
    if len(m) != 2:
        m = "0" + m
    if len(s) != 2:
        s = "0"+ s
    digital = h + ":" + m + ":" + s
    return digital


class Timer:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.hr = hours
        self.min = minutes
        self.sec = seconds

    def __str__(self):
        return clock(self.hr, self.min, self.sec)

    def next_second(self):
        if self.sec < 59:
            self.sec += 1
        else:
            self.sec = 0
            if self.min < 59:
                self.min += 1
            else:
                self.min = 0
                if self.hr < 23:
                    self.hr += 1
                else:
                    self.hr = 0

    def prev_second(self):
        if self.sec > 0:
            self.sec -= 1
        else:
            self.sec = 59
            if self.min > 0:
                self.min -= 1
            else:
                self.min = 59
                if self.hr > 0:
                    self.hr -= 1
                else:
                    self.hr = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
