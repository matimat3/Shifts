import random

employeesArray = [
    "Employe1",
    "Employe2",
    "Employe3",
    "Employe4",
    "Employe5",
    "Employe6",
    "Employe7",
    "Employe8",
    "Employe9",
    "Employe10",
    "Employe11",
    "Employe12",
    "Employe13",
    "Employe14",
]

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
        if len(shiftEarly) < earlyShiftNeeded:
            shiftEarly.append(x)
        elif len(shiftMid) < midShiftNeeded:
            shiftMid.append(x)
        elif len(shiftLate) < lateShiftNeeded:
            shiftLate.append(x)
        else:
            notAssigned.append(x)

    print("Early shift: ")
    print(shiftEarly)
    print("Mid shift: ")
    print(shiftMid)
    print("Late shift: ")
    print(shiftLate)
    print("Rest: ")
    print(notAssigned)


# def differentShift(): # if someone is in a given shift, he can't be assigned to another one

shiftMaker()
