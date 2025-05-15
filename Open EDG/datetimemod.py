import datetime


dt = datetime.datetime(2020, 11, 4, 14, 53)
a = dt.strftime("%Y/%m/%d %H:%M:%S")
print(a)
a = dt.strftime("%y/%B/%d %H:%M:%S %p")
print(a)
a = dt.strftime("%a, %Y %b %d")
print(a)
a = dt.strftime("%A, %Y %B %d")
print(a)
a = dt.strftime("%w")
print("Weekday: ", a)
a = dt.strftime("%j")
print("Day of the year: ", a)
a = dt.strftime("%W")
print("Week number of the year: ", a)
