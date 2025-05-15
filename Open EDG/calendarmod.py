import calendar as c


class MyCalendar(c.Calendar):
    def count_weekday_in_year(self, year, weekday):
        count = 0
        for i in range(1, 13):
            for week in self.monthdays2calendar(year, i):
                for dom, dow in week:
                    if dow == weekday and dom != 0:
                        count += 1
        return count


print(MyCalendar().count_weekday_in_year(2019, c.MONDAY))
