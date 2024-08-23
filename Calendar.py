import numpy as np
from tabulate import tabulate

class Calendar():

    def __init__(self):

        self.calendar = []
        for month in np.arange(0,12,1):
            if month in [0,2,4,6,7,9,11]:
                self.calendar.append(np.arange(1,31+1,1).tolist())
            if month in [3,5,8,10]:
                self.calendar.append(np.arange(1,30+1,1).tolist())
            if month == 1:
                self.calendar.append(np.arange(1,28+1,1).tolist())
        
    def add_start_end_date(self, start_date, end_date):
        self.calendar[start_date[0]] =self.calendar[start_date[0]][start_date[1]-1:len(self.calendar[start_date[0]])]
        self.calendar[end_date[0]] =self.calendar[end_date[0]][0:end_date[1]]
        self.calendar =self.calendar[start_date[0]:end_date[0]+1]

if __name__ == '__main__':
    calendar = Calendar()
    print(tabulate(calendar.calendar))
    calendar.add_start_end_date([8,9],[10,11])
    print(tabulate(calendar.calendar))