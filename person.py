class Person:

    def __init__(self, name, missing_dates):
        self.name = name
        self.missing_dates = missing_dates
    
    def addMissing(self, date):
        self.missing_dates.append(date)

    def __str__(self):
        string = str(self.name) + ' - ' + str(self.missing_dates)
        return string

if __name__ == '__main__':
    pass