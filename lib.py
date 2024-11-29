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
    file_ptr_to_add.write(' '.join(['\n' + str(count), '||', title, '||', author, '||', year, '||', 'в наличии']))
    file_ptr_to_add.close()

    print('Adding a new book was successful!')

def read(id=-1):

    print('Library List:')

    file_ptr_to_read = open('library.txt', 'r')
    text = file_ptr_to_read.readlines()

    for lines in text:
        if id == -1:
            for part in lines.split():
                if not (part == '||' or part == 'наличии' or part == 'выдана'):
                    print(part, end = ' ')
                elif not part == '||':
                    print(part, end = '\n')
        elif id == lines.split()[0]:
            for part in lines.split():
                if not (part == '||' or part == 'наличии' or part == 'выдана'):
                    print(part, end = ' ')
                elif not part == '||':
                    print(part, end = '\n')

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
   
def change_status(id):

    file_ptr_to_copy = open('library.txt', 'r')
    records = file_ptr_to_copy.readlines()
    file_ptr_to_copy.close()

    file_ptr_to_write = open('library.txt', 'w')
    for record in records:
        if record.split()[0] == id:
            record = record.split()
            if record[-1] == 'выдана':
                record[-1] = 'в наличии'
            else:
                record[-2] = 'выдана'
                record[-1] = ''
            record = ' '.join(record)
        file_ptr_to_write.write(record)
    file_ptr_to_write.close()
    
    print('The change in the status of the book was successful!')

def find_book(title, author, year):
    file_ptr_to_copy = open('library.txt', 'r')
    records = file_ptr_to_copy.readlines()
    file_ptr_to_copy.close()
    for record in records:
        parts = [0, 0, 0, 0]
        parts_index = 0
        count = 0
        clone_record = record.split()
        for part in clone_record:
            if part == '||':
                parts[parts_index] = count
                parts_index += 1
            count += 1
        rec_title = None
        if not title == None:
            rec_title = ''.join(clone_record[parts[0]+1:parts[1]])
        rec_author = None
        if not author == None:
            rec_author = ''.join(clone_record[parts[1]+1:parts[2]])
        rec_year = None
        if not year == None:
            rec_year = ''.join(clone_record[parts[2]+1:parts[3]])
        if title == rec_title and author == rec_author and year == rec_year:
            read(clone_record[0])

exit = 1
while True and exit:

    count = sort()

    print("""What do you want to do?
a - to add a new book
c - to change the status of the book
d - to delete the book
f - to finding the book
s - to showing all books
q - to exiting the program""")
    
    user_choice = input()
    clean_screen()
    if user_choice == 'a':
        add(count)
    elif user_choice == 'c':
        print('Which record do you want to change status?\nEnter id')
        id = input()
        change_status(id)
    elif user_choice == 'd':
        print('Which record do you want to delete?\nEnter id')
        delete(input())
        sort()
    elif user_choice == 'f':
        title = None
        author = None
        year = None
        print('Поиск будет по Названию? (y-Y/n-N)')        
        answer = input()     
        if (answer == 'y' or answer == 'Y'):
            print('Введите Название книги')
            title = input()
        print('Поиск будет по Имени автора книги? (y-Y/n-N)')        
        answer = input()     
        if (answer == 'y' or answer == 'Y'):
            print('Введите Имя автора книги')
            author = input()
        print('Поиск будет по Году издания? (y-Y/n-N)')
        answer = input()     
        if (answer == 'y' or answer == 'Y'):
            print('Введите Год издания книги')
            year = input()
        find_book(title, author, year)
    elif user_choice == 's':
        read()
    elif user_choice == 'q':
        break
    
    while True:
        print('Continue working? (y-Y/n-N(exit))')
        go_on = input()
        if go_on == 'n' or go_on == 'N':
            exit = 0
            clean_screen()
            break
        elif go_on == 'y' or go_on == 'Y':
            clean_screen()
            break
        else:
            clean_screen()