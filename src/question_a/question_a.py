#write functions here, don't add input('') statements here!

def create_multiplication_table():
    table = []
    for row in range(1,6):
        row_list = []
        for col in range(1, 11):
            row_list.append(row*col)
        table.append(row_list)
    return table

def display_multiplication_table(table):
    for row in table:
        for value in row:
            print(f"{value:3}", end="")
        print()
