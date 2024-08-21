import numpy as np
from Calendar import Calendar
from tabulate import tabulate

class Person:

    def __init__(self, name):
        self.name = name
        self.calendar = Calendar()
        self.rested = True
    
    def addMissing(self, *dates):
        for date in dates:
            self.calendar.calendar[date[0]][date[1]] = 'X'

    def getTotalCleaningDays(self):
        sum = 0
        for month in self.calendar.calendar:
            for day in month:
                if day == 'X':
                    sum += 1
        return sum
    
    def getCleaningDays(self):
        pass

if __name__ == '__main__':
    person = Person('Jonathan')
    person.addMissing([1,3],[4,5])
    print(tabulate(person.calendar.calendar))
    print(person.getTotalCleaningDays())