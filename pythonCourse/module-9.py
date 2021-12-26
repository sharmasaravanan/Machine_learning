
# datetime,
import datetime as dt

t = dt.datetime.now()

print(t)
print("date:", t.date())
print('hour  :', t.hour)
print('minute:', t.minute)
print('second:', t.second)
print('microsecond:', t.microsecond)
print('tzinfo:', t.tzinfo)

print('Resolution:', dt.time.resolution)

today = dt.date.today()
print(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())
print('Year:', today.year)
print('Mon :', today.month)
print('Day :', today.day)

print('Today    :', today)

one_day = dt.timedelta(days=4)
print('One day  :', one_day)

yesterday = today - one_day
print('Yesterday:', yesterday)

tomorrow = today + one_day
print('Tomorrow :', tomorrow)

print('tomorrow - yesterday:', tomorrow - yesterday)
print('yesterday - tomorrow:', yesterday - tomorrow)

# calendar module
import calendar as cal
c = cal.TextCalendar(cal.MONDAY)
print(c.formatmonth(2021, 8))

c = cal.HTMLCalendar(cal.SUNDAY)
print(c.formatmonth(2021, 9))

for name in cal.month_name:
    print(name)

for name in cal.day_name:
    print(name)

print(cal.calendar(2021))

print(cal.isleap(2018))

# error handling
try:
    print(a)
except:
    print("There is an error")
print("hello world")

try:
    print(a)
except Exception as e:
    print("There is an error :", e)
print("hello world")



# prime number check
def isPrimeCheck(num):
    for j in range(2, num):
        if num % j == 0:
            break
    else:
        return num
try:
    i = int(input('enter any number'))
except:
    print("Entered number is not integer")
    i =15

try:
    ans = isPrimeCheck(i)
except Exception as e:
    print("There is an error :", e)
    ans = None
if ans:
    print(ans)
