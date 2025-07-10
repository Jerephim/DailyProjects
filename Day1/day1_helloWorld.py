def helloWorldBasic(): #This function outputs Hello World! after each part of the phrase is stored in variables.
    h = "Hello"
    w = "world"
    exclamation = "!"
    print(f"{h} {w}{exclamation}")
    
def helloWorldInteractive(): #This is a function that says hi to the user after they give their first and last name.
    first = input("\nWhat is your first name?\n>>> ")
    last = input("\nWhat is your last name?\n>>> ")
    print(f"\nHello {first} {last}. I hope you have a great day")

def displayMenu(): #This function outputs the menu for the user to chose their experience.
    print("--Please pick an option--\n\t1) basic\n\t2) interactive")
    
def error(): #This function is used to let the user know that they need to enter either a 1 or a 2 when prompted.
    print("You were supposed to pick either 1 or 2 by typing 1 or 2 and then pressing enter. Please try again")
    
def pickMenuOption(choice): #This function handles the logic depending on which option the user chooses.
    if choice == 1:
        helloWorldBasic()
    elif choice == 2:
        helloWorldInteractive()
    else: #This case catches all incorrect inputs.
        error()
        
def main(): #Calls all functions
    displayMenu()
    choice = int(input(">>> "))
    pickMenuOption(choice)
    buffer = input("\n\nPress Enter to close")

main() #This Runs the program and this is a test