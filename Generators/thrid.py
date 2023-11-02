import datetime


def generate_dow(month, day, year):
    start_date = datetime.date(year, month, day)
    days_of_week = ['Понедельник', 'Вторник', 'Среда',
                    'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    while True:
        dow = days_of_week[start_date.weekday()]
        yield dow
        start_date += datetime.timedelta(days=1)


i = 0
for dow in generate_dow(10, 25, 2023):
    if i == 5:
        break
    print(dow)
    i += 1

for i in range(10):
    print(i)