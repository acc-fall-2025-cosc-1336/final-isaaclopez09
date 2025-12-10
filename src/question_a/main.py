#add import
from question_a import create_multiplication_table, display_multiplication_table

def main():
    running = True
    while running:
        print("Main menu")
        print("1 - Display multiplication table.")
        print("2 - Exit")
        selection = input("Enter your selection here: ")
        print("")
        if selection == "1":
            table = create_multiplication_table()
            display_multiplication_table(table)
            print("")
            print("select 1 to continue or 2 to exit")
            print("")
        elif selection == "2":
            print("Exiting program")
            break
        else:
            print("Invalid option, try again.")
            print("")

if __name__ == '__main__':
    main()
