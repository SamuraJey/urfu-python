import datetime


def generate_dates(month, day, year):
    start_date = datetime.date(year, month, day)
    while True:
        yield start_date
        start_date += datetime.timedelta(days=1)


for date in generate_dates(1, 1, 2023):
    if date.year == 2024:
        break
    print(date)
