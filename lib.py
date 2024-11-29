def clean_screen():
    print("\033[H\033[J", end="")

def sort():

    file_ptr_to_sort = open('library.txt', 'r')
    records = file_ptr_to_sort.readlines()
    file_ptr_to_sort.close()

    file_ptr_to_sort = open('library.txt', 'w')
    count = 0
    for record in records:
        buf = record.split()
        buf[0] = str(count)
        count+=1
        file_ptr_to_sort.write(' '.join(buf))
        if not str(record) == str(''.join(records[-1:])):
            file_ptr_to_sort.write('\n')
    file_ptr_to_sort.close()
    return count

def add(count):
    
    print('Вводите построчно.')
    print('title:')
    title=input()
    print('author:')
    author=input()
    print('year:')
    year=input()
    file_ptr_to_add = open('library.txt', 'a')
    file_ptr_to_add.write(' '.join(['\n', str(count), title, author, year, 'в наличии']))
    file_ptr_to_add.close()

    print('Adding a new book was successful!')

def read():

    print('Library List:')

    file_ptr_to_read = open('library.txt', 'r')
    print(file_ptr_to_read.read())
    file_ptr_to_read.close()

def delete(id):

    file_ptr_to_copy = open('library.txt', 'r')
    records = file_ptr_to_copy.readlines()
    file_ptr_to_copy.close()

    file_ptr_to_write = open('library.txt', 'w')
    for record in records:
        if not record.split()[0] == id:
            file_ptr_to_write.write(record)
    file_ptr_to_write.close()

    print('Deleting the book was successful.')
   
exit = 1
while True and exit:

    count = sort()

    print("""What do you want to do?
a - to add a new book
d - to delete the book
f - to finding the book
s - to showing all books
q - to exiting the program""")

    user_choice = input()
    clean_screen()
    if user_choice == 'a':
        add(count)
    elif user_choice == 'd':
        print('Какую запись удалить?\nВведите id')
        delete(input())
        sort()
    if user_choice == 'f':
        # add(count)
        print('f')
    elif user_choice == 's':
        read()
    elif user_choice == 'q':
        break
    
    while True:
        print('Continue working? (y/n)')
        go_on = input()
        if go_on == 'n':
            exit = 0
            clean_screen()
            break
        elif go_on == 'y':
            clean_screen()
            break
        else:
            clean_screen()