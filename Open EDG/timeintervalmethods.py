def form(hour, mn, sec):
    H = str(hour) if hour > 10 else "0" + str(hour)
    M = str(mn) if mn > 10 else "0" + str(mn)
    S = str(sec) if sec > 10 else "0" + str(sec)
    return H + ":" + M + ":" + S


class TimeInt:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.h = hours
        self.m = minutes
        self.s = seconds
        self.ts = hours * 3600 + minutes * 60 + seconds

    def __str__(self):
        return form(self.h, self.m, self.s)

    def __add__(self, other):
        if isinstance(other, TimeInt):
            o = other.ts
        elif isinstance(other, int):
            o = other
        else:
            raise TypeError
        total = self.ts + o
        H = total // 3600
        r = total % 3600
        M = r // 60
        S = r % 60
        return TimeInt(H, M, S)

    def __sub__(self, other):
        if isinstance(other, TimeInt):
            o = other.ts
        elif isinstance(other, int):
            o = other
        else:
            raise TypeError
        total = self.ts - o
        H = total // 3600
        r = total % 3600
        M = r // 60
        S = r % 60
        return TimeInt(H, M, S)

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError
        total = self.ts * other
        H = total // 3600
        r = total % 3600
        M = r // 60
        S = r % 60
        return TimeInt(H, M, S)


fti = TimeInt(21, 58, 50)
sti = TimeInt(1, 45, 22)

print(fti)
print(sti)
print(fti + 62)
print(fti - 62)
print(fti * 2)




# example answer below
#
#
class TimeInterval:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __add_sub(self, other, operation_type):
        own = self.hours * 3600 + self.minutes * 60 + self.seconds
        another = other.hours * 3600 + other.minutes * 60 + other.seconds

        if operation_type == 'subtraction':
            new_time = own - another
        elif operation_type == 'addition':
            new_time = own + another
        else:
            raise Exception('Unknown operation')

        new_hours = new_time // 3600
        new_minutes = (new_time % 3600) // 60
        new_seconds = new_time % 60

        return TimeInterval(hours=new_hours, minutes=new_minutes, seconds=new_seconds)

    def __add__(self, other):
        if isinstance(other, TimeInterval):
            return self.__add_sub(other, 'addition')
        elif isinstance(other, int):
            return self.__add_sub(TimeInterval(seconds=other), 'addition')
        else:
            raise TypeError('can only add TimeInterval or integer objects')

    def __sub__(self, other):
        if isinstance(other, TimeInterval):
            return self.__add_sub(other, 'subtraction')
        elif isinstance(other, int):
            return self.__add_sub(TimeInterval(seconds=other), 'subtraction')
        else:
            raise TypeError('can only subtract TimeInterval objects')

    def __mul__(self, other):
        if isinstance(other, int):
            new_time = (self.hours * 3600 + self.minutes * 60 + self.seconds) * other
            new_hours = new_time // 3600
            new_minutes = (new_time % 3600) // 60
            new_seconds = new_time % 60
            return TimeInterval(hours=new_hours, minutes=new_minutes, seconds=new_seconds)
        else:
            raise TypeError('can only multiply TimeInterval objects by integers  ')

    def __str__(self):
        return "%s:%s:%s" % (self.hours, self.minutes, self.seconds)
t1 = TimeInterval(hours=21, minutes=58, seconds=50)
t2 = TimeInterval(1, 45, 22)

assert str(t1 + t2) == '23:44:12'
assert str(t1 - t2) == '20:13:28'
assert str(t1 * 2) == '43:57:40'
assert str(t1 + 62) == '21:59:52'
assert str(t1 - 62) == '21:57:48'

