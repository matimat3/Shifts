import random
from random import randint


class Employee:
    favShiftCounter = 0

    def __init__(self, name, favouriteShift, lastShift):
        self.name = name
        self.favouriteShift = favouriteShift
        self.lastShift = lastShift


# 60/100 fav shift, 20/100 each other
# if fav shift not got: 80/100 fav shift, 10/100 each other

Employee1 = Employee("Leon", 0, 1)
Employee2 = Employee("Biki", 0, 2)

print(Employee1.name)
print(Employee1.favouriteShift)
print(Employee1.lastShift)

employeesArray = [Employee1, Employee2]

print(employeesArray)

earlyShiftNeeded = 3
midShiftNeeded = 4
lateShiftNeeded = 5

shiftEarly = [0]
shiftMid = [0]
shiftLate = [0]

notAssigned = [0]

shiftEarly.pop(0)
shiftMid.pop(0)
shiftLate.pop(0)
notAssigned.pop(0)


def shiftMaker():
    random.shuffle(employeesArray)
    for x in employeesArray:
        if x.favouriteShift == 0:
            randomNum = randint(0, 100)
            print(randomNum)
            if randomNum <= 60:
                print("EARLY SHIFT")
                print(randomNum)
            elif randomNum > 60 & randomNum <= 80:
                print("MID SHIFT")

        print("fav shift: ")
        print(x.favouriteShift)
    else:
        print("not fav shift")


# def differentShift(): # if someone is in a given shift, he can't be assigned to another one

shiftMaker()
