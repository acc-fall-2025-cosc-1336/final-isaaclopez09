from question_b import stock, get_stock_list

def main():
    Stock_data = get_stock_list()
    running = True
    while running:
        print("Main menu")
        print("1 - Display stock purchase history")
        print("2 - Exit")
        selection = input("Enter your selection here: ")
        print("")
        if selection == "1":
            print("Stock Report:")
            for stock in Stock_data:
                print(f"symbol: {stock.get_symbol()}, company: {stock.get_company_name()}")
            print("")
        elif selection == "2":
            print("Exiting the program")
            break
        else:
            print("Invalid option, try again.")
            print("")

if __name__ == '__main__':
    main()