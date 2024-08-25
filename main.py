from person import Person
from Calendar import Calendar
import numpy as np
from tabulate import tabulate
from userInterface import Table
from tkinter import *
from scheduler import Scheduler

#

# ------------------------add people-----------------------------#

jonathan = Person('Jonathan')
kristina = Person('Kristina')
ron = Person('Ron')
maja = Person('Maja')

jonathan.addMissing([10,22])
maja.addMissing([9,11],[9,12],[9,13],[7,16],[7,17])
ron.addMissing([7,16],[7,17])
ron.addMissingRange([8,11],[10,5])

people = [jonathan, kristina, ron, maja]

# --------------start/end date to schedule for-------------------#

start_date = [7,10]
end_date = [11,20]

# ----------------------run scheduler----------------------------#
scheduler = Scheduler(people, start_date, end_date)
scheduler.schedule()

root = Tk()
t = Table(root, scheduler)
root.mainloop()