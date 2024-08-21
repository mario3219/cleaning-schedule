from person import Person
import numpy as np
from Calendar import Calendar
from tabulate import tabulate

# test

class Scheduler:
    def __init__(self, people, start_date, end_date):
        self.people = people
        self.start_date = start_date
        self.end_date = end_date
        for person in people:
            self.add_start_end_date(person, start_date, end_date)

    
    def addPerson(self, person):
        self.people.append(person)
    
    def add_start_end_date(self, person, start_date, end_date):
        person.calendar.calendar[start_date[0]] = [person.calendar.calendar[start_date[0]][0]] + person.calendar.calendar[start_date[0]][start_date[1]:len(person.calendar.calendar[start_date[0]])]
        person.calendar.calendar[end_date[0]] = [person.calendar.calendar[end_date[0]][0]] + person.calendar.calendar[end_date[0]][1:end_date[1]+1]
        person.calendar.calendar = person.calendar.calendar[start_date[0]:end_date[0]+1]
    
    def schedule(self):
        pass

if __name__ == '__main__':
    people = [Person('Jonathan'), Person('Kristina')]
    scheduler = Scheduler(people, [8,10], [11,30])
    print(tabulate(people[0].calendar.calendar))