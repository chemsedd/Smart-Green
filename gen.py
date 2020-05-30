import calendar

for y in range(2009, 2021):
    for m in range(1, 13):
        for d in range(calendar.monthrange(y, m)[1]):
            print(calendar.month_name[m])

"""
for i in range(1, 13):
    _2020 = calendar.monthrange(2020, i)
    for d in range(1, _2020[1] + 1):
        print(d)

        """