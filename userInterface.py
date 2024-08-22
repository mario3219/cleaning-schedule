from tkinter import *
from scheduler import Scheduler
from person import Person
import numpy as np
from tabulate import tabulate
from Calendar import Calendar
 
class Table:
     
    def __init__(self,root):
         
        # code for creating table

            for i in range(total_rows):
                for j in range(total_columns):
                    name = lst[i][0]
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
                    self.e.insert(END, lst[i][j])
 
# take the datadwdawddwdwdwdwd dwdwd

people = [Person('Jonathan'), Person('Kristina'), Person('Ron'), Person('Maja')]
people[0].addMissing([10,22])
people[0].addMissing([9,11],[9,12],[9,13])
scheduler = Scheduler(people, [9,10], [11,20])
scheduler.schedule()

def longest(list1):
    longest_list = max(len(elem) for elem in list1)
    return longest_list

lst = []
months = np.arange(scheduler.start_date[0],scheduler.end_date[0]+1,1)
width = longest(people[0].calendar.calendar)

temp = Person('temp')
scheduler.add_start_end_date(temp, [9,10], [11,20])

for idx in np.arange(0, scheduler.end_date[0]-scheduler.start_date[0]+1,1).tolist():
    if months[idx] == 0:
        lst.append(['January'])
    elif months[idx] == 1:
        print('February')
    elif months[idx] == 2:
        print('Mars')
    elif months[idx] == 3:
        print('April')
    elif months[idx] == 4:
        print('May')
    elif months[idx] == 5:
        print('June')
    elif months[idx] == 6:
        print('July')
    elif months[idx] == 7:
        print('August')
    elif months[idx] == 8:
        print('September')
    elif months[idx] == 9:
        lst.append(['October'] + ['-']*width)
    elif months[idx] == 10:
        lst.append(['November'] + ['-']*width)
    elif months[idx] == 11:
        lst.append(['December'] + ['-']*width)
    for person in people:
        lst.append([person.name] + temp.calendar.calendar[idx] + ['-']*(width-len(person.calendar.calendar[idx])))
print(tabulate(people[0].calendar.calendar))
print(tabulate(temp.calendar.calendar))

# print(len(lst[0]), len(lst[1]), len(lst[2]))
# print(width)
# print(lst[0])
# print(lst[1])
# print(lst[2])
# print(lst[0][0], lst[0][1])

# lst = [['-'], ['-']]
  
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[1])
  
# create root window
root = Tk()
t = Table(root)
root.mainloop()