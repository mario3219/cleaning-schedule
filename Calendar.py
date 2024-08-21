import numpy as np
from tabulate import tabulate

class Calendar():

    def __init__(self):

        self.calendar = []
        for month in np.arange(0,12,1):
            if month in [0,2,4,6,7,9,11]:
                if month == 0:
                    month_name = 'January'
                if month == 2:
                    month_name = 'Mars'
                if month == 4:
                    month_name = 'May'
                if month == 6:
                    month_name = 'July'
                if month == 7:
                    month_name = 'August'
                if month == 9:
                    month_name = 'October'
                if month == 11:
                    month_name = 'December'
                self.calendar.append([month_name] + np.arange(1,31+1,1).tolist())
            if month in [3,5,8,10]:
                if month == 3:
                    month_name = 'April'
                if month == 5:
                    month_name = 'June'
                if month == 8:
                    month_name = 'September'
                if month == 10:
                    month_name = 'November'
                self.calendar.append([month_name] + np.arange(1,30+1,1).tolist())
            if month == 1:
                self.calendar.append(['February'] + np.arange(1,28+1,1).tolist())

if __name__ == '__main__':
    calendar = Calendar()
    calendar.calendar[1][1] = 'X'
    print(tabulate(calendar.calendar))