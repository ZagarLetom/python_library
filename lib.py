def clean_screen():
    print("\033[H\033[J", end='')

def sort():

    file_ptr_to_sort = open("library.txt", "r")
    records = file_ptr_to_sort.readlines()
    file_ptr_to_sort.close()

    file_ptr_to_sort = open("library.txt", "w")
    count = 0
    for record in records:
        if not record[0] == '\n' and not record[0] == '':
            buf = record.split()
            buf[0] = str(count)
            count += 1
            file_ptr_to_sort.write(' '.join(buf))
            if not str(record) == str(' '.join(records[-1])):
                file_ptr_to_sort.write('\n')
    file_ptr_to_sort.close()
    return count


def add(count):

    print("Вводите построчно.")
    print("title:")
    title = input()
    print("author:")
    author = input()
    print("year:")
    year = input()
    file_ptr_to_add = open("library.txt", "a")
    file_ptr_to_add.write(
        ' '.join(
            [
                "\n" + str(count),
                "||",
                title,
                "||",
                author,
                "||",
                year,
                "||",
                "в наличии",
            ]
        )
    )
    file_ptr_to_add.close()

    clean_screen()
    print(title, author, year)
    print("Adding a new book was successful!\n")


def read(id=-1):

    file_ptr_to_read = open("library.txt", "r")
    text = file_ptr_to_read.readlines()
    file_ptr_to_read.close()
    
    max_title_length = 0
    max_author_size = 0
    max_count = 0
    for lines in text:
        buf_title_length = 0
        buf_author_size = 0
        string = lines.split()
        if int(string[0]) > max_count:
            max_count = int(string[0])
        i = 2
        intervals = -1
        while not string[i] == '||':
            buf_title_length += len(string[i])
            intervals += 1
            i += 1
        i += 1
        buf_title_length += intervals
        intervals = -1
        while not string[i] == '||':
            buf_author_size += len(string[i])
            intervals += 1
            i += 1
        buf_author_size += intervals
        if buf_title_length > max_title_length:
            max_title_length = buf_title_length
        if buf_author_size > max_author_size:
            max_author_size = buf_author_size

    if max_count > 2:
        for i in range(0, max_count - 2):
            print(' ', end = '')
    print('id', end = ' ')
    print('title', end = '')
    if max_title_length > 4:
        for i in range(0, max_title_length - 5 + 1):
            print(' ', end = '')
    else:
        print('\t', end = '')
    print('author', end = '')
    if max_title_length > 5:
        for i in range(0, max_author_size - 6 + 1):
            print(' ', end = '')
    else:
        print('\t', end = '')
    print('\t', 'year', '\t', 'status', sep = '')

    for lines in text:
        if id == -1 or id == lines.split()[0]:
            parts = lines.split()
            # вывод цифры
            for j in range(0, max_count - len(parts[0])):
                print(' ', end = '')
            print(parts[0], end = ' ')

            # вывод названия
            i = 2
            buf_length = 0
            intervals = 0
            while not parts[i] == '||':
                intervals += 1
                buf_length += len(parts[i])
                print(parts[i], end = ' ')
                i += 1
            i += 1
            buf_length += intervals - 1
            for j in range(0, max_title_length - buf_length):
                print(' ', end = '')
            
            # вывод имени автора
            buf_length = 0
            intervals = 0
            while not parts[i] == '||':
                intervals += 1
                buf_length += len(parts[i])
                print(parts[i], end = ' ')
                i += 1
            i += 1
            buf_length += intervals - 1
            for j in range(0, max_author_size - buf_length):
                print(' ', end = '')
            print('\t', parts[i], sep = '', end = '\t')
            i += 2
            if parts[i] == 'в':
                print(parts[i], end = ' ')
                print(parts[i + 1])
            else:
                print(parts[i])

def delete(id):

    file_ptr_to_copy = open("library.txt", "r")
    records = file_ptr_to_copy.readlines()
    file_ptr_to_copy.close()

    file_ptr_to_write = open("library.txt", "w")
    for record in records:
        if not record.split()[0] == id:
            file_ptr_to_write.write(record)
    file_ptr_to_write.close()

    print("Deleting the book was successful.\n")


def change_status(id):

    file_ptr_to_copy = open("library.txt", "r")
    records = file_ptr_to_copy.readlines()
    file_ptr_to_copy.close()

    file_ptr_to_write = open("library.txt", "w")
    match = False
    for record in records:
        if record.split()[0] == id:
            match = True
            record = record.split()
            if record[-1] == "выдана":
                record[-1] = "в наличии"
            else:
                record[-2] = "выдана"
                record[-1] = ''
            record = ' '.join(record)
        file_ptr_to_write.write(record)
    file_ptr_to_write.close()

    if match:
        print('The change in the status of the book was successful!\n')
    else:
        if id.isdigit():
            print('Записи с id - ' + id + ' не существует.')
        else:
            print('id - ' + id + ' - не число.')

def find_book(title, author, year):
    file_ptr_to_copy = open("library.txt", "r")
    records = file_ptr_to_copy.readlines()
    file_ptr_to_copy.close()
    print("Library List:")
    for record in records:
        parts = [0, 0, 0, 0]
        parts_index = 0
        count = 0
        clone_record = record.split()
        for part in clone_record:
            if part == "||":
                parts[parts_index] = count
                parts_index += 1
            count += 1
        rec_title = ''
        if not title == '':
            rec_title = ''.join(clone_record[parts[0] + 1 : parts[1]])
        rec_author = ''
        if not author == '':
            rec_author = ''.join(clone_record[parts[1] + 1 : parts[2]])
        rec_year = ''
        if not year == '':
            rec_year = ''.join(clone_record[parts[2] + 1 : parts[3]])
        if title == rec_title and author == rec_author and year == rec_year:
            read(clone_record[0])
    print()

exit = 1
while True and exit:

    count = sort()

    print("""What do you want to do?\nEnter - to continue
    a - to add a new book
    c - to change the status of the book
    d - to delete the book
    f - to finding the book
    s - to showing all books
    q/quit/exit/clear - to exiting the program"""
    )

    user_choice = input()
    clean_screen()
    if user_choice == "a":
        add(count)
    elif user_choice == "c":
        print("Which record do you want to change status?\nEnter id")
        id = input()
        change_status(id)
    elif user_choice == "d":
        print("Which record do you want to delete?\nEnter id (or last or first)")
        id = input()
        if id == 'last':
            id = count - 1
        elif id == 'first':
            id = 0
        delete(id)
        sort()
    elif user_choice == "f":

        print("Поиск будет по Названию? (y-Y/n-N)")
        title = input()

        print("Поиск будет по Имени автора книги? (y-Y/n-N)")
        author = input()

        print('Поиск будет по Году издания? "Enter" - to skip')
        year = input()

        find_book(title, author, year)
    elif user_choice == "s":
        print("Library List:")
        read()
        print()
    elif user_choice == "q" or user_choice == "quit" or user_choice == "exit" or user_choice == "clear":
        break
    while True:
        print("Continue working?\n  n/N - to exit\nEnter - to continue")
        go_on = input()
        if go_on == "n" or go_on == "N" or go_on == "exit" or go_on == "clear":
            exit = 0
            clean_screen()
            break
        else:
            clean_screen()
            break