from person import Person
import numpy as np
from Calendar import Calendar
from tabulate import tabulate

class Scheduler:
    def __init__(self, people, start_date, end_date):
        self.people = people
        self.start_date = start_date
        self.end_date = end_date
        for person in self.people:
            self.add_start_end_date(person, start_date, end_date)

    
    def addPerson(self, person):
        self.add_start_end_date(person, self.start_date, self.end_date)
        self.people.append(person)
    
    def add_start_end_date(self, person, start_date, end_date):
        person.calendar.calendar[start_date[0]] = person.calendar.calendar[start_date[0]][start_date[1]-1:len(person.calendar.calendar[start_date[0]])]
        person.calendar.calendar[end_date[0]] = person.calendar.calendar[end_date[0]][0:end_date[1]]
        person.calendar.calendar = person.calendar.calendar[start_date[0]:end_date[0]+1]
    
    def schedule(self):

        temp = self.people[0].calendar.calendar
        sum_days_per_person = 0
        for month in temp:
            for day in month:
                sum_days_per_person += 1
            sum_days_per_person -= 1
        sum_days_per_person = sum_days_per_person*2/len(self.people)
        
        dates_pair1 = []
        dates_pair2 = []

        for person in self.people:
            rest_days = 0
            for month in person.calendar.calendar:
                for day in month:
                    idxmonth = person.calendar.calendar.index(month)
                    idxday = person.calendar.calendar[idxmonth].index(day)
                    if day != 'X' and [idxmonth,idxday] not in dates_pair1 and person.rested:
                        person.calendar.calendar[idxmonth][idxday] = 'H'
                        dates_pair1.append([idxmonth,idxday])
                        rest_days += 1
                    elif day != 'X' and [idxmonth,idxday] not in dates_pair2 and person.rested:
                        person.calendar.calendar[idxmonth][idxday] = 'H'
                        dates_pair2.append([idxmonth,idxday])
                        rest_days += 1
                    if rest_days == 0:
                        person.rested = True
                    if rest_days == 7:
                        person.rested = False
                    if not person.rested:
                        rest_days -= 1
                    if person.getTotalCleaningDays() > sum_days_per_person:
                        break
    
    def printSchedule(self):
        months = np.arange(self.start_date[0],self.end_date[0]+1,1)
        for idx in np.arange(0, self.end_date[0]-self.start_date[0]+1,1).tolist():
            if months[idx] == 0:
                print('January')
            if months[idx] == 1:
                print('February')
            if months[idx] == 2:
                print('Mars')
            if months[idx] == 3:
                print('April')
            if months[idx] == 4:
                print('May')
            if months[idx] == 5:
                print('June')
            if months[idx] == 6:
                print('July')
            if months[idx] == 7:
                print('August')
            if months[idx] == 8:
                print('September')
            if months[idx] == 9:
                print('October')
            if months[idx] == 10:
                print('November')
            if months[idx] == 11:
                print('December')
            temp = []
            for person in self.people:
                temp.append([person.name] + person.calendar.calendar[idx])
            print(tabulate(temp))

if __name__ == '__main__':
    calendar = Calendar()
    people = [Person('Jonathan'), Person('Kristina'), Person('Ron'), Person('Maja')]
    people[0].addMissing([10,22])
    people[0].addMissing([9,11],[9,12],[9,13])
    print(tabulate(people[0].calendar.calendar))
    scheduler = Scheduler(people, [9,10], [11,20])
    scheduler.schedule()

    for month in np.arange(0,len(people[0].calendar.calendar),1).tolist():
        table = []
        for person in people:
            table.append([person.name] + person.calendar.calendar[month])
        if month == 0:
            print('Oktober')
        if month == 1:
            print('November')
        if month == 2:
            print('December')
        print(tabulate(table))
    
    print(np.arange(9,11+1,1))
    print(np.arange(0,11-9+1,1))
    scheduler.printSchedule()