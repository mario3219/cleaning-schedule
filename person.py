import numpy as np

class Person:

    def __init__(self, name, missing_dates):
        self.name = name
        self.missing_dates = missing_dates
        self.cleaning_dates = []
        self.rested = True
        self.cleaning_streak = 0
        self.rest_days = 0
    
    def addMissing(self, date):
        self.missing_dates.append(date)
        self.calibrateMissingDates()

    def calibrateMissingDates(self):
        idx = 0
        while idx < len(self.missing_dates):
            if idx + 1 == len(self.missing_dates):
                break
            diff = self.missing_dates[idx+1] - self.missing_dates[idx]
            if diff < 3:
                missing_dates = np.arange(self.missing_dates[idx]+1, self.missing_dates[idx+1], 1)
                missing_dates = missing_dates.tolist()
                self.missing_dates = self.missing_dates[0:idx+1] + missing_dates + self.missing_dates[idx+1:len(self.missing_dates)]
            idx += 1
    
    def getTotalCleaningDays(self):
        sum = 0
        for day in self.cleaning_dates:
            if day == 'X':
                sum += 1
        return sum

    def __str__(self):
        string = str(self.name) + ' - ' + str(self.missing_dates)
        return string

if __name__ == '__main__':
    pass