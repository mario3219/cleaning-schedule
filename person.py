import numpy as np
from Calendar import Calendar
from tabulate import tabulate

class Person:

    def __init__(self, name):
        self.name = name
        self.calendar = Calendar()
        self.rested = True
        self.rest_days = 0
        self.cleaning_streak = 0

    def addMissing(self, *dates):
        for date in dates:
            self.calendar.calendar[date[0]][date[1]] = 'X'
    
    def addMissingRange(self, start_date, end_date):
        temp = Calendar()
        temp.add_start_end_date(start_date, end_date)
        idxmonths = np.arange(start_date[0], end_date[0]+1, 1).tolist()
        idx = 0
        for month in temp.calendar:
            for day in month:
                self.addMissing([idxmonths[idx], day-1])
            idx += 1
            
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
    temp = Person('temp')
    print(tabulate(temp.calendar.calendar))
    temp.addMissingRange([9,10], [11,20])
    print(tabulate(temp.calendar.calendar))