def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else: return True

def days_in_month(year, month):
    if is_year_leap(year):
        months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month - 1 not in range(len(months)):
        return None
    else:
        return months[month - 1]

def day_of_year(year, month, day):
    if days_in_month(year, month) == None:
        return None
    elif day-1 not in range(days_in_month(year, month)):
        return None
    else: 
        return str(month) + "/" + str(day) + "/" + str(year)
    
print(day_of_year(2000, 0, 32))
