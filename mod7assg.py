from datetime import *
from random import randint
def timeStuff():
    dateTime = datetime.now()
    date, time = str(dateTime).split()
    print("{0}\t{1}".format(date, time))
    #By making seconds = -60 I'm making it so that when I add it to the date
    #it'll actually subtract instead. It'll output the current date and time
    #exatly 60 seconds behind though.
    modifier = timedelta(seconds=-60)
    print(dateTime + modifier)
    #By making weeks = 104 I'm making it so that when I add it to the date
    #it'll add two years.
    modifier = timedelta(weeks=104)
    print(dateTime + modifier)

    delta = timedelta(days=100, hours=10, minutes=13)
def distCalculator(feet, inches):
    t = randint(1, 30)
    td = timedelta(seconds = t)
    distance = (feet*12)+inches
    startTime = datetime.now()
    endTime = startTime + td
    perSecond = distance/t
    void, startTime = str(startTime).split()
    startTime, void = str(startTime).split(".")
    void, endTime = str(endTime).split()
    endTime, void = str(endTime).split(".")
    overview = "The object went {} inches in {} seconds.".format(distance, t)
    timeStuff = "It started at {} and is currently at {}.".format(startTime, endTime)
    result = "Thus, it went {:10.2f}in./sec for {} seconds.".format(perSecond, t)
    print(overview)
    print(timeStuff)
    print(result)
def main():
    timeStuff()
    feet = int(input("How many feet did the object travel? "))
    inches = int(input("How many inches did the object travel? "))
    distCalculator(feet, inches)
main()
