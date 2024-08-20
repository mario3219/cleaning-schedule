from person import Person
from Calendar import Calendar
import numpy as np
from tabulate import tabulate

person1 = Person('p1', [1, 3, 5, 7])
person2 = Person('p2', [])
person3 = Person('p3', [])
person4 = Person('p4', [])
people = [person1, person2, person3, person4]
for person in people:
    print(person)

calendar = Calendar(11, 12)

print(calendar.getCalendar())

person1.calibrateMissingDates()
print(person1)
totaldays = 14
print(totaldays)
person1_table = calendar.calendar[0]
print(person1_table)

sumdays = 0
rest = 0
okay = True
for day in person1_table:
    if day not in person1.missing_dates and okay:
        person1_table[person1_table.index(day)] = 'X'
        sumdays += 1
        rest += 1
    if rest == 0:
        okay = True
    elif rest == 7:
        okay = False
    if not okay:
        rest -= 1
    if sumdays > totaldays:
        break
print(person1_table)