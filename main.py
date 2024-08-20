from person import Person
from Calendar import Calendar
import numpy as np
from tabulate import tabulate

person1 = Person('p1', [1, 3, 5])
person2 = Person('p2', [])
person3 = Person('p3', [])
person4 = Person('p4', [])
people = [person1, person2, person3, person4]
for person in people:
    print(person)

calendar = Calendar(11, 12)

print(calendar.getCalendar())
