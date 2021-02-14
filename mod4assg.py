#The root I'm finding is x^2-5.86x+8.5408
#a = 1, b = -5.86, c = 8.5408
import math
def roots():
    a = 1
    b = -5.86
    c = 8.5408
    leftMostB = b * -1
    middleB = b * 2
    rightMostStuff = 4 * a * c
    allUnderRoot = middleB - rightMostStuff
    if(allUnderRoot < 0):
        allUnderRoot = allUnderRoot * -1
    sqrt = math.sqrt(allUnderRoot)
    negative = (-b - sqrt)/(2*a)
    positive = (-b + sqrt)/(2*a)
    print("The Positive quadratic equation roots are " + str(positive))
    print("The Negative quadratic equation roots are " + str(negative))
def reciprocals():
    for i in range(1,11):
        print("The decimal version of 1/" + str(i) + " equals: " + str(1/i))
roots()
reciprocals()
