import numpy as np
from tabulate import tabulate

class Calendar():

    def __init__(self, start_month, end_month):

        m1 = start_month
        m2 = end_month

        self.range = np.arange(m1,m2,1)
        self.calendar = []

        for month in self.range:
            if month in [0,2,4,6,7,9,11]:
                list = np.arange(1,31+1,1)
                list = list.tolist()
                self.calendar.append(list)
            if month in [3,5,8,10]:
                list = np.arange(1,30+1,1)
                list = list.tolist()
                self.calendar.append(list)
            if month == 1:
                list = np.arange(1,28+1,1)
                list = list.tolist()
                self.calendar.append(list)

    def getCalendar(self):
        table = []
        for idx in np.arange(0,len(self.range),1):
            if self.range[idx] == 0:
                table.append(['January', str(self.calendar[idx])])
            if self.range[idx] == 1:
                table.append(['Februari', str(self.calendar[idx])])
            if self.range[idx] == 2:
                table.append(['Mars', str(self.calendar[idx])])
            if self.range[idx] == 3:
                table.append(['April', str(self.calendar[idx])])
            if self.range[idx] == 4:
                table.append(['Maj', str(self.calendar[idx])])
            if self.range[idx] == 5:
                table.append(['Juni', str(self.calendar[idx])])
            if self.range[idx] == 6:
                table.append(['Juli', str(self.calendar[idx])])
            if self.range[idx] == 7:
                table.append(['Augusti', str(self.calendar[idx])])
            if self.range[idx] == 8:
                table.append(['September', str(self.calendar[idx])])
            if self.range[idx] == 9:
                table.append(['Oktober', str(self.calendar[idx])])
            if self.range[idx] == 10:
                table.append(['November', str(self.calendar[idx])])
            if self.range[idx] == 11:
                table.append(['December', str(self.calendar[idx])])
        return tabulate(table)