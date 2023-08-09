from datetime import date
from datetime import datetime

print(datetime.today())


today = datetime.today()


print(type(today))

today_date = date.today()

type(today_date)

today_date.month

today_date.year

today_date.day

mybirthday = date(today_date.year, 11, 25)

if mybirthday != today_date:
    print("It's not my birthday, I need wait "  + str((mybirthday - today_date).days) + " until there.")
else:
    print("Crontulations it's my birth day \o/")