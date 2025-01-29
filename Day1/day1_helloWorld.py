def helloWorldBasic():
    h = "Hello"
    w = "world"
    exclamation = "!"
    print(f"{h} {w}{exclamation}")
    
def helloWorldInteractive():
    first = input("\nWhat is your first name?\n>>> ")
    last = input("\nWhat is your last name?\n>>> ")
    print(f"\nHello {first} {last}. I hope you have a great day")

def displayMenu():
    print("--Please pick an option--\n\t1) basic\n\t2) interactive")
    
def error():
    print("You were supposed to pick either 1 or 2 by typing 1 or 2 and then pressing enter. Please try again")
    
def pickMenuOption(choice):
    if choice == 1:
        helloWorldBasic()
    elif choice == 2:
        helloWorldInteractive()
    else:
        print()

displayMenu()
choice = int(input(">>> "))
pickMenuOption(choice)
buffer = input("\n\n\Press Enter to close")
