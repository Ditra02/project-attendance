import os


def menu():
    os.system("cls")
    print("Menu".center(13, "~"))
    print("1.Input Data")
    print("2.Update Data")
    print("3.Delete Data")
    print("4.Read Data")
    print("5.Delete file")
    print("6.Quit")
    opsi = int(input("Angka Opsi >> "))
    return opsi


def input_data(line):
    if line == 1:
        with open("my_file.txt", "w") as my_file:
            my_file.write("%-3s %-22s %15s\n" % ('No', 'Nama', 'Nim'))

    name = input("%-7s:" % ('Name'))
    nim = input("%-7s:" % ('Nim'))
    print()

    # *how much remain space from 35 char (distance beetween Name column and Nim column)
    spaces = (35 - len(name)) * " "

    with open("my_file.txt", "a") as my_file:
        my_file.write(f"{line}   {name.title()}{spaces}{nim}\n")


def read_line():
    """
    Returns:
        sum_line: a number of line stored in file exclude header
    """
    with open("my_file.txt", "r") as my_file:
        sum_line = len(my_file.readlines())
        # * first line is header
    return sum_line


def read_data():
    os.system('cls')
    # ?detect how many row in file
    rows = read_line()

    print("Student Attendance".center(55, '~').title())
    with open("my_file.txt", "r") as my_file:
        while rows != 0:
            print(my_file.readline().strip('\n'))
            rows -= 1


def update_data():
    """[Note]
    Args:
        data ([list]): [use for store old data in the file]
    """

    data = []
    with open('my_file.txt', 'r+') as my_file:
        data = my_file.readlines()

    iteration_update = int(input('How Many row you want to be update >> '))

    for update in range(iteration_update):
        read_data()

        line_opt = int(input("Which line you want to update >> "))
        name = input("%-7s:" % ('Name'))
        nim = input("%-7s:" % ('Nim'))
        print()

        # *how much remain space from 35 char (distance beetween Name column and Nim column)
        spaces = (35 - len(name)) * " "
        new_data = f"{line_opt}   {name.title()}{spaces}{nim}\n"

        # *delete old_data in list then append the new_data
        data.pop(line_opt)
        data.insert(line_opt, new_data)

        # ? writing the list of data which contain new data to file
        with open('my_file.txt', 'r+') as my_file:
            my_file.writelines(data)


def delete_data():
    read_data()
    data = []
    with open('my_file.txt', 'r+') as my_file:
        data = my_file.readlines()

    # * ask input separated by space
    rows_deleted = input('The rows you want to remove >> ').split()
    rows_deleted = [int(row) for row in rows_deleted]  # * convert to int

    # ?update empty data as '' in order to keep the sequence of row
    for idx in range(len(rows_deleted)):
        # *pick and replace the index of old data
        data.insert(rows_deleted[idx], '')
        data.pop(rows_deleted[idx] + 1)  # *delete old data in next 1 index

    # ?deleting '' from list
    idx = 0
    while (idx < len(data)):
        if data[idx] == '':
            data.pop(idx)
        idx += 1

    # ?delete row's number and reset numbering
    no = 1
    for row in range(1, len(data)):
        data[row] = str(no) + " " * (4 - len(str(no))) + data[row][4:]
        no += 1

    with open('my_file.txt', 'w') as my_file:
        my_file.writelines(data)

    read_data()
    os.system('pause')


while(1):
    option = menu()

    if option == 1:
        os.system("cls")
        num_data = int(input("\nHow many data that will be inputted >> "))

        try:
            line_already = read_line()          # *if file exist before program runs
        except FileNotFoundError:
            line_already = 1                    # *if file doesn't exist

        # * the number of row after data have inputted
        reachLine = line_already + num_data

        for row in range(line_already, reachLine):
            input_data(row)
    elif option == 2:
        read_data()
        update_data()
    elif option == 3:
        delete_data()
    elif option == 4:
        read_data()
        os.system('pause')
    elif option == 5:
        os.remove('my_file.txt')
        print('my_file.txt deleted')
    elif option == 6:
        os.system("cls")
        quit()
