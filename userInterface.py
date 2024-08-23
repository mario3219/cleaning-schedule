from tkinter import *
from scheduler import Scheduler
from person import Person
import numpy as np
from tabulate import tabulate
from Calendar import Calendar
 
# test

class Table:
     
    def __init__(self, root, scheduler):
         
        # code for creating table

        temp = Calendar()
        temp.add_start_end_date(scheduler.start_date, scheduler.end_date)

        months = np.arange(scheduler.start_date[0],scheduler.end_date[0]+1,1)
        width = max(len(elem) for elem in scheduler.people[0].calendar.calendar)

        lst = []
        templst = []
        for idx in np.arange(0, scheduler.end_date[0]-scheduler.start_date[0]+1,1).tolist():
            if months[idx] == 0:
                lst.append(['January'] + ['-']*width)
                templst.append(['January'] + ['-']*width)
            elif months[idx] == 1:
                lst.append(['February'] + ['-']*width)
                templst.append(['February'] + ['-']*width)
            elif months[idx] == 2:
                lst.append(['Mars'] + ['-']*width)
                templst.append(['Mars'] + ['-']*width)
            elif months[idx] == 3:
                lst.append(['April'] + ['-']*width)
                templst.append(['April'] + ['-']*width)
            elif months[idx] == 4:
                lst.append(['May'] + ['-']*width)
                templst.append(['May'] + ['-']*width)
            elif months[idx] == 5:
                lst.append(['June'] + ['-']*width)
                templst.append(['June'] + ['-']*width)
            elif months[idx] == 6:
                lst.append(['July'] + ['-']*width)
                templst.append(['July'] + ['-']*width)
            elif months[idx] == 7:
                lst.append(['August'] + ['-']*width)
                templst.append(['August'] + ['-']*width)
            elif months[idx] == 8:
                lst.append(['September'] + ['-']*width)
                templst.append(['September'] + ['-']*width)
            elif months[idx] == 9:
                lst.append(['October'] + ['-']*width)
                templst.append(['October'] + ['-']*width)
            elif months[idx] == 10:
                lst.append(['November'] + ['-']*width)
                templst.append(['November'] + ['-']*width)
            elif months[idx] == 11:
                lst.append(['December'] + ['-']*width)
                templst.append(['December'] + ['-']*width)
            for person in scheduler.people:
                lst.append([person.name] + person.calendar.calendar[idx] + ['-']*(width-len(person.calendar.calendar[idx])))
                templst.append([person.name] + temp.calendar[idx] + ['-']*(width-len(person.calendar.calendar[idx])))

        total_rows = len(lst)
        total_columns = len(lst[1])

        for i in range(total_rows):
            for j in range(total_columns):
                if lst[i][1] == '-':
                    self.e = Entry(root, width=5, fg='black',
                            font=('Arial',10,'bold'))
                elif j == 0:
                    self.e = Entry(root, width=10, fg='black',
                            font=('Arial',10))
                else:
                    self.e = Entry(root, width=5, fg='black',
                            font=('Arial',10))
                    if lst[i][j] == 'H':
                        self.e.configure(background='green')
                    elif lst[i][j] == 'X':
                        self.e.configure(background='red')
                    else:
                        self.e.configure(background='white')
                self.e.grid(row=i, column=j)
                self.e.insert(END, templst[i][j])

if __name__ == '__main__':

    people = [Person('Jonathan'), Person('Kristina'), Person('Ron'), Person('Maja')]
    people[0].addMissing([10,22])
    people[0].addMissing([9,11],[9,12],[9,13])
    scheduler = Scheduler(people, [6,10], [11,20])
    scheduler.schedule()
    
    # create root window
    root = Tk()
    t = Table(root, scheduler)
    root.mainloop()