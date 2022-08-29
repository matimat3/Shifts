import random
from random import randint


class Employee:
    favShiftCounter = 0

    def __init__(self, name, favouriteShift, lastShift, weight):
        self.name = name
        self.favouriteShift = favouriteShift
        self.lastShift = lastShift
        self.weight = weight


# 60/100 fav shift, 20/100 each other
# if fav shift not got: 80/100 fav shift, 10/100 each other

Employee1 = Employee("Employee 1", "Early Shift", "Late Shift", 0)
Employee2 = Employee("Employee 2", "Middle Shift", "Late Shift", 0)


employeesArray = [Employee1, Employee2]


earlyShiftNeeded = 3
midShiftNeeded = 4
lateShiftNeeded = 5

shiftEarlyArray = [0]
shiftMidArray = [0]
shiftLateArray = [0]

notAssigned = [0]

shiftEarlyArray.pop(0)
shiftMidArray.pop(0)
shiftLateArray.pop(0)
notAssigned.pop(0)


def shiftMaker():
    random.shuffle(employeesArray)
    for x in employeesArray:
        randomNum = randint(0, 100)
        print(randomNum)
        if randomNum <= x.weight:
            x.lastShift = "Early Shift"
        elif randomNum > x.weight & randomNum <= x.weight + 20:
            x.lastShift = "Middle Shift"
        elif randomNum > x.weight + 20:
            x.lastShift = "Late Shift"
        if x.lastShift == x.favouriteShift:
            print("Favourite shift obtained")
            x.weight = 60
        elif x.lastShift != x.favouriteShift:
            x.weight += 20

        print("fav shift: ")
        print(x.favouriteShift)


# def differentShift(): # if someone is in a given shift, he can't be assigned to another one

shiftMaker()
