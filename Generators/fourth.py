import datetime


def generate_dates_and_dow(month, day, year, count=10):
    for date, dow in zip(generate_dates(month, day, year), generate_dow(month, day, year)):
        count -= 1
        # need to yield in tuple, not in two separate yields
        yield (date, dow)
        if count == 1:
            break


def generate_dates(month, day, year):
    start_date = datetime.date(year, month, day)
    while True:
        yield start_date
        start_date += datetime.timedelta(days=1)


def generate_dow(month, day, year):
    start_date = datetime.date(year, month, day)
    days_of_week = ['Понедельник', 'Вторник', 'Среда',
                    'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    while True:
        dow = days_of_week[start_date.weekday()]
        yield dow
        start_date += datetime.timedelta(days=1)


for q in generate_dates_and_dow(10, 25, 2023):
    print(q)
    print(q[0], q[1])