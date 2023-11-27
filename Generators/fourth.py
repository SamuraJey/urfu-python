import second
import thrid


def generate_dates_and_dow(month, day, year, count=10):
    for date, dow in zip(second.generate_dates(month, day, year), thrid.generate_dow(month, day, year)):
        count -= 1
        yield (date, dow)
        if count == 1:
            break


for q in generate_dates_and_dow(10, 25, 2023):
    print(q)
    print(q[0], q[1])
