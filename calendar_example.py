import calendar as cal

c = cal.TextCalendar(cal.SUNDAY)
print(c.formatmonth(2019, 9))

import calendar as cal

c = cal.HTMLCalendar(cal.SUNDAY)
print(c.formatmonth(2019, 9))

for name in cal.month_name:
    print(name)

for name in cal.day_name:
    print(name)

print(cal.calendar(2012))

cal.isleap(2018)
