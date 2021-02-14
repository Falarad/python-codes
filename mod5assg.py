def execute():
    code = input("Please input a line of code. ")
    exec(code)
def insert():
    base = "Hello!"
    i = ""
    while(i != "yes"):
        insert = input("Please input the string you want to add. ")
        location = int(input("At what index would you like to place your string? "))
        base = base[:location] + insert + base[location:]
        print(base)
        i = input("Are the changes to your liking? Input 'yes' if so.")
def main():
    execute()
    insert()
main()
        
