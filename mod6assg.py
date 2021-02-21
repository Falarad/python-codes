#Below I'm defining a Point object. It's pretty boring with just a x and y value.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #Below I'm defining what to do if the object is turned into a string.
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

#Defining Rectangle.
class Rectangle:
    def __init__(self, point, width, height):
        self.corner = point
        self.width = width
        self.height = height
    #Same string function, a little more involved though.
    def __str__(self):
        return "The top left corner is {0}, with a width of {1} and a height of {2}".format(self.corner, self.width, self.height)

    #The next two definitions are class functions. To call the below one for example is Rectangle.shiftRectangle
    def shiftRectangle(self, dx, dy):
        point = self.corner
        point.x = point.x + dx
        point.y = point.y + dy
        return True

    def offsetRectangle(self, dx, dy):
        point = self.corner
        newRectX = point.x + dx
        newRectY = point.y + dy
        return Rectangle(Point(newRectX, newRectY), self.width, self.height)

#Creating a rectangle without the use of the Point class
def create_rectangle(x, y, width, height):
    return Rectangle(Point(x, y), width, height)

def str_rectangle(rect):
    return str(rect)

def help():
    print("Type 'new' to create a new rectangle.")
    print("Type 'print' to print an existing rectangle.")
    print("Type 'offset' to make an offset of a rectangle.")
    print("Type 'shift' to shift a rectangle.")
    print("Type 'quit' to exit the program.")

#The next four functions are for the userInterface function. It takes the user through doing the action it's dedicated for.
def newRect(dictionary):
    x = input("Please input the x coordinate. ")
    y = input("Please input the y coordinate. ")
    width = input("Please input the width. ")
    height = input("Please input the height. ")
    name = input("Please input the name. ")
    vars = [x, y, width, height]
    try:
        for var in vars:
            var = int(var)
        dictionary[name] = create_rectangle(x, y, width, height)
        return dictionary
    except:
        print("A parameter or name was not valid. Returning to interface...")

def printRect(dictionary):
    name = input("Please input the name of the rectangle you want to print. ")
    try:
        print(str_rectangle(dictionary[name]))
    except:
        print("Name invalid. Returning to interface...")

def offsetRect(dictionary):
    name = input("Please input the name of the rectangle you want to offset. ")
    try:
        target = dictionary[name]
        dx = int(input("Please input the distance from the previous x coordinate. "))
        dy = int(input("Please input the distance from the previous y coordinate. "))
        newName = input("Please input the name of the new rectangle. ")
        dictionary[newName] = target.offsetRectangle(dx, dy)
        return dictionary
    except:
        print("Name or distance invalid. Returning to interface...")

def shiftRect(dictionary):
    name = input("Please input the name of the rectangle you want to shift. ")
    try:
        target = dictionary[name]
        dx = input("Please input the distance from the previous x coordinate. ")
        dy = input("Please input the distance from the previous y coordinate. ")
        target.shiftRectangle(dx, dy)
        return dictionary
    except:
        print("Name or distance invalid. Returning to interface...")

#userInterface is a pretty cool function.
#rectDict is a dictionary for the rectangles to be stored in.
#tempList is so that I can pull the names of the rectangles and display them.
def userInterface():
    rectDict = {}
    tempList = []
    quit = False
    while(quit != True):
        for key, val in rectDict.items():
            tempList.append(key)
        print("Current rectangles: " + tempList)
        userInput = input("> ").casefold()
        if(userInput == "quit"):
            quit = True
        elif(userInput == "new"):
            rectDict = newRect(rectDict)
        elif(userInput == "print"):
            printRect(rectDict)
        elif(userInput == "offset"):
            rectDict = offsetRect(rectDict)
        elif(userInput == "shift"):
            rectDict = shiftRect(rectDict)
        elif(userInput == "help"):
            help()
        else:
            print("I cannot understand, please try again.")
        tempList = []

def tests():
    r1 = create_rectangle(10, 20, 30, 40)
    print(str_rectangle(r1))
    r1.shiftRectangle(-10, -20)
    print(str_rectangle(r1))
    r2 = r1.offsetRectangle(100, 100)
    print(str_rectangle(r1))
    print(str_rectangle(r2))
    print("Okay, clearing all rectangles...")
    del(r1, r2)

def main():
    tests()
    print("Now you can make your own!")
    help()
    print("Please type 'help' if you need any future guidance.")
    userInterface()

main()
