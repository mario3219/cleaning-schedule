from person import Person
from Calendar import Calendar
import numpy as np
from tabulate import tabulate
from userInterface import Table
from tkinter import *
from scheduler import Scheduler

#

# ------------------------add people-----------------------------#

theo = Person('Theo')
joakim = Person('Joakim')
hugo = Person('Hugo')
joana = Person('Joana')
sara = Person('Sara')
german = Person('German')
yx = Person('YX')
marzia = Person('Marzia')

# theo.addMissingRange([5,21],[7,8])
# hugo.addMissingRange([5,11],[7,18])
# joana.addMissingRange([5,25],[7,18])
# german.addMissingRange([6,8],[6,14])
# yx.addMissingRange([5,4],[6,4])
# yx.addMissingRange([7,3],[7,10])
# marzia.addMissingRange([5,17],[7,18])

people = [theo, joakim, hugo, joana, sara, german, yx, marzia]

# --------------start/end date to schedule for-------------------#

start_date = [5,3]
end_date = [7,18]

# ----------------------run scheduler----------------------------#
scheduler = Scheduler(people, start_date, end_date)
scheduler.schedule()

root = Tk()
t = Table(root, scheduler)
root.mainloop()