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
            person.calendar.add_start_end_date(start_date, end_date)

    
    def addPerson(self, person):
        person.calendar.add_start_end_date(start_date, end_date)
        self.people.append(person)
    
    def schedule(self):

        temp = Calendar()
        temp.add_start_end_date(self.start_date, self.end_date)
        sum_days_per_person = 0
        # for month in temp.calendar:
        #     for day in month:
        #         sum_days_per_person += 1
        #     sum_days_per_person -= 1
        # sum_days_per_person = sum_days_per_person*2/len(self.people)
        
        dates_pair1 = []
        dates_pair2 = []
        diff = self.end_date[0] - self.start_date[0]
        indexes_months = np.arange(0, diff+1, 1)
        print(indexes_months)
        for month in indexes_months:
            for day in temp.calendar[month]:
                for person in self.people:
                    idxmonth = month
                    idxday = temp.calendar[idxmonth].index(day)
                    if person.calendar.calendar[idxmonth][idxday] != 'X' and [idxmonth,idxday] not in dates_pair1 and person.rested:
                        person.calendar.calendar[idxmonth][idxday] = 'H'
                        dates_pair1.append([idxmonth,idxday])
                        person.rest_days += 1
                    elif person.calendar.calendar[idxmonth][idxday] != 'X' and [idxmonth,idxday] not in dates_pair2 and person.rested:
                        person.calendar.calendar[idxmonth][idxday] = 'H'
                        dates_pair2.append([idxmonth,idxday])
                        person.rest_days += 1
                    if person.rest_days == 0:
                        person.rested = True
                    if person.rest_days == 7:
                        person.rested = False
                    if not person.rested:
                        person.rest_days -= 1
                    # if person.getTotalCleaningDays() > sum_days_per_person:
                    #     break
                if [idxmonth,idxday] not in dates_pair1 or dates_pair2:
                    person_with_longest_rest = self.people[0]
                    for person in self.people:
                        if person.rest_days > person_with_longest_rest.rest_days:
                            person_with_longest_rest = person
                    person_with_longest_rest.calendar.calendar[idxmonth][idxday] = 'H'
                    dates_pair1.append([idxmonth,idxday])
                    person_with_longest_rest.rest_days += 1

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
    jonathan = Person('Jonathan')
    kristina = Person('Kristina')
    ron = Person('Ron')
    maja = Person('Maja')

    jonathan.addMissing([10,22])
    maja.addMissing([9,11],[9,12],[9,13],[7,16],[7,17])
    ron.addMissing([7,16],[7,17])
    ron.addMissingRange([8,11],[10,5])

    people = [jonathan, kristina, ron, maja]
    scheduler = Scheduler(people, [6,10], [11,20])
    scheduler.schedule()
    scheduler.printSchedule()