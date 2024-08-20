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

    def calibrateMissingDates(self):
        idx = 0
        while idx < len(self.missing_dates):
            if idx + 1 == len(self.missing_dates):
                break
            value1 = self.missing_dates[idx]
            value2 = self.missing_dates[idx+1]
            diff = value2 - value1
            if diff < 3:
                missing_dates = np.arange(value1+1, value2, 1)
                missing_dates = missing_dates.tolist()
                self.missing_dates = self.missing_dates[0:idx+1] + missing_dates + self.missing_dates[idx+1:len(self.missing_dates)]
            idx += 1

    def __str__(self):
        string = str(self.name) + ' - ' + str(self.missing_dates)
        return string

if __name__ == '__main__':
    pass