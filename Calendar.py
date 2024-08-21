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

if __name__ == '__main__':
    pass