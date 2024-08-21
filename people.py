from person import Person
import numpy as np
from Calendar import Calendar
from tabulate import tabulate

# test

class People:
    def __init__(self, people, calendar):
        self.people = people
        self.calendar = calendar
    
    def addPerson(self, person):
        self.people.append(person)
    
    def calcCleaningSchedule(self):
        days_per_person = len(self.calendar.calendar[0])*2/len(self.people)
        taken_dates_pair1 = []
        taken_dates_pair2 = []
        for person in self.people:
            person.calibrateMissingDates()
            person.cleaning_dates = self.calendar.calendar[0].copy()
            for day in person.cleaning_dates:
                if day not in person.missing_dates and day not in taken_dates_pair1 and person.rested:
                    person.cleaning_dates[person.cleaning_dates.index(day)] = 'X'
                    taken_dates_pair1.append(day)
                    person.cleaning_streak += 1
                    person.rest_days += 1
                elif day not in person.missing_dates and day not in taken_dates_pair2 and person.rested:
                    person.cleaning_dates[person.cleaning_dates.index(day)] = 'X'
                    taken_dates_pair2.append(day)
                    person.cleaning_streak += 1
                    person.rest_days += 1
                if person.rest_days == 0:
                    person.rested = True
                elif person.rest_days == 7:
                    person.rested = False
                if not person.rested:
                    person.rest_days -= 1
                if person.cleaning_streak > days_per_person:
                    break
    
    def printFinishedSchedule(self):
        table = []
        for person in self.people:
            dates = person.cleaning_dates.copy()
            for date in dates:
                date = str(date)
            table.append([person.name] + dates)
            print(person.getTotalCleaningDays)
        print(tabulate(table))
    
    def getPeople(self):
        list = []
        for person in self.people:
            list.append(person.__str__())
        return list

if __name__ == '__main__':
    person1 = Person('p1', [1, 3, 5, 7])
    person2 = Person('p2', [1, 7])
    person3 = Person('p3', [])
    person4 = Person('p4', [])
    people = [person1, person2, person3, person4]
    calendar = Calendar(11, 12)
    people = People(people, calendar)

    people.calcCleaningSchedule()
    people.printFinishedSchedule()