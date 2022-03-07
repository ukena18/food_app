import datetime

#
# d = datetime.date(2001,5,12)
# print(d)


tday = datetime.date.today()
# print(tday)
# print(tday.year)
# print(tday.isoweekday())

tdelta = datetime.timedelta(days=2)
# print(tdelta)


# print(tday+tdelta)
# print(tday-tdelta)

# date2 = date1 + timedelta
# timedelta = date1+date2

bday = datetime.date(2023,1,18)
till_bday = bday - tday


# print(till_bday)




import datetime
#
# t = datetime.time(1,2,3,40000)
# print(t)

dt = datetime.datetime(2023,1,2,12,23,43,12000)

# print(dt.date())
# print(dt.time())
# print(dt.year)

tdelta = datetime.timedelta(hours = 2)

dt = dt + tdelta
print(dt)