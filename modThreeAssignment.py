def greeting(names):
    for i in names:
        print("Hello {}!".format(i))
        print("It is lovely to meet you {}.".format(i))
        print("Well, goodbye {}.".format(i))
def fullNames(firstName, lastName):
    print("Hello, " + firstName + " " + lastName + ".")
def additionCalculator(numOne, numTwo):
    print("The sum of {} and {} is {}.".format(numOne, numTwo, numOne+numTwo))
def returnCalculator(numOne, numTwo):
    return numOne + numTwo
def main():
    names = ['Miguel', 'Lisa', 'Joanna']
    firstName = 'Miguel'
    lastName = 'Pimentel'
    numOne = 27
    numTwo = 44
    greeting(names)
    fullNames(firstName, lastName)
    additionCalculator(numOne, numTwo)
    returned = returnCalculator(numOne, numTwo)
    print("The sum of {} and {} is {}.".format(numOne, numTwo, returned))
main()
