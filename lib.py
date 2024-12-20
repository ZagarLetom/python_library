class Library:

    def add_new_book(self):
        new_id = str(self.ordering_id()[0])
        default_value = 'unknown'
        default_status = 'в наличии'
        print('Вводите построчно.')
        print('title:')
        title = input()
        if title == '':
            title = default_value
        print('author:')
        author = input()
        if author == '':
            author = default_value
        print('year:')
        year = input()
        if year == '':
            year = '2024'
        while not year.isdigit():
            print('ОШИБКА - ' + year + ' - это не число!\nВведите год издания книги')
            print('year:')
            year = input()
        file_ptr_to_add = open('library.txt', 'a')
        new_record = '^'.join(
                [
                    new_id,
                    title,
                    author,
                    year,
                    default_status,
                    '\n'
                ]
            )
        contents = self.readlines_from_file()
        if len(contents) > 0:
            if contents[-1].split('^')[-1] == '\n':
                file_ptr_to_add.write(new_record)
            else:
                file_ptr_to_add.write('\n' + new_record)
        else:
            file_ptr_to_add.write(new_record)
        file_ptr_to_add.close()

        if int(year) > 2024:
            print(year + ' - год издания книги?\nСмешно. Но ладно.\n')
        
        print('\nNEW BOOK!\n')
        self.print_out_record_info(new_record)
        print("\nAdding a new book was successful!\n")

    def change_book_status(self):

        print('Which record do you want to change status?\nEnter id')

        id = input()

        if id == 'last':
            id = str(self.ordering_id()[0] - 1)

        records = self.readlines_from_file()

        file_ptr_to_write = open('library.txt', 'w')
        match = False
        change_record = False
        for record in records:
            if record.split('^')[0] == id:
                match = True
                print('\nOld Status:\n')
                self.print_out_record_info(record)
                record = record.split('^')
                if record[-2] == 'выдана':
                    record[-2] = 'в наличии'
                else:
                    record[-2] = 'выдана'
                record = '^'.join(record)
                change_record = record
            file_ptr_to_write.write(record)
        file_ptr_to_write.close()

        if match:
            print('\nNEW STATUS!\n')
            self.print_out_record_info(change_record)
            print('\nThe change in the status of the book was successful!\n')
        else:
            self.check_correct_id(id)

    def delete_book(self):

        print('Which record do you want to delete?\nEnter id')
        
        id = input()

        if id == 'last':
            id = str(self.ordering_id()[0] - 1)

        records = self.readlines_from_file()

        match = False
        deleted_record = False
        file_ptr_to_write = open('library.txt', 'w')
        for record in records:
            if not record.split('^')[0] == id:
                file_ptr_to_write.write(record)
            else:
                match = True
                deleted_record = record
        file_ptr_to_write.close()

        if match:
            print('\nDeleted Record:\n')
            self.print_out_record_info(deleted_record)
            print('\nDeleting the book was successful.\n')
        else:
            self.check_correct_id(id)

    def find_book(self):

        print('Поиск будет по Названию? "Enter" - to skip')
        title = input()

        print('Поиск будет по Имени автора? "Enter" - to skip')
        author = input()

        print('Поиск будет по Году издания? "Enter" - to skip')
        year = input()

        records = self.readlines_from_file()

        print('Search result:')

        book_been_found = False

        # Поиск по точному совпадению
        for record in records:
            rec_title, rec_author, rec_year = self.extract_title_author_year(record, title, author, year)
            if title == rec_title and author == rec_author and year == rec_year:
                self.print_out_record_info(record, not book_been_found)
                book_been_found = True

        # Поиск по подстрокам, если ничего не найдено по точному поиску
        if not book_been_found:
            for record in records:
                rec_title, rec_author, rec_year = self.extract_title_author_year(record, title, author, year)
                if title in rec_title and author in rec_author and year in rec_year:
                    self.print_out_record_info(record, not book_been_found)
                    book_been_found = True

        if not book_been_found:
            print('\t>>There are no such books in our library :(')
        print()

    def show_all(self):
        print('Library List:')
        records = self.readlines_from_file()
        first_out = True
        for record in records:
            self.print_out_record_info(record, first_out)
            first_out = False
        if first_out:
            print('\t>>There are no such books in our library :(')
        print()

    def print_out_record_info(self, record, first_out=True):
        record = record.split('^')
        max_id, max_title, max_author = self.ordering_id()
        max_id -= 1
        max_id = str(max_id)
        if first_out:
        # Вывод описания таблицы
            print(' ' * (len(max_id) - 2) + 'id',
            'title' + ' ' * (max_title - 5),
            'author' + ' ' * (max_author - 6),
            'year',
            'status',
            sep = '\t')
        # Вывод информации о книге
        print(' ' * (len(max_id) - len(record[0])) + record[0],
            record[1] + ' ' * (max_title - len(record[1])),
            record[2] + ' ' * (max_author - len(record[2])),
            record[3],
            record[4],
            sep = '\t')

    def ordering_id(self):

        records = self.readlines_from_file()

        current_possible_id = 0
        max_len_title = 0
        max_len_author = 0

        if len(records) > 0:
            file_ptr_to_sort = open('library.txt', 'w')
            for record in records:
                rec_list = record.split('^')
                rec_list[0] = str(current_possible_id)
                file_ptr_to_sort.write('^'.join(rec_list))
                current_possible_id += 1
                if len(rec_list[1]) > max_len_title:
                    max_len_title = len(rec_list[1])
                if len(rec_list[2]) > max_len_author:
                    max_len_author = len(rec_list[2])
            file_ptr_to_sort.close()
        return current_possible_id, max_len_title, max_len_author

    def extract_title_author_year(self, record, title, author, year):
        record = record.split('^')
        rec_title = ''
        if not title == '':
            rec_title = record[1]
        rec_author = ''
        if not author == '':
            rec_author = record[2]
        rec_year = ''
        if not year == '':
            rec_year = record[3]
        return rec_title, rec_author, rec_year

    def readlines_from_file(self):
        try:
            source_file = open('library.txt', 'r')
        except FileNotFoundError :
            source_file = open('library.txt', 'w')
        finally:
            source_file.close()
        source_file = open('library.txt', 'r')
        records = source_file.readlines()
        source_file.close()
        return records

    def check_correct_id(self, id):
        if id.isdigit():
            print('\nОШИБКА: Записи с id - ' + id + ' не существует.\n')
        else:
            print('\nОШИБКА: "номер" id - ' + id + ' - не число.\n')

def clean_screen():
    print('\033[H\033[J', end='')

def main_menu_options(quit_list):
    exit = False
    user_choice = input()
    clean_screen()
    if user_choice == 'a' or user_choice == 'A' or user_choice == 'ф' or user_choice == 'Ф':
        our_Library.add_new_book()
    elif user_choice == 'c' or user_choice == 'C' or user_choice == 'с' or user_choice == 'С':
        our_Library.change_book_status()
    elif user_choice == 'd' or user_choice == 'D' or user_choice == 'в' or user_choice == 'В':
        our_Library.delete_book()
    elif user_choice == 'f' or user_choice == 'F' or user_choice == 'а' or user_choice == 'А':
        our_Library.find_book()
    elif user_choice == 's' or user_choice == 'S' or user_choice == 'ы' or user_choice == 'Ы':
        our_Library.show_all()
    else:
        for out_com in quit_list:
            if user_choice == out_com:
                exit = True
    return exit

def additionnal_menu_options(quit_list):
    exit = False
    print('Continue working?\n  n/N - to exit\nEnter - to continue')
    go_on = input()
    for out_com in (['n', 'т', 'N', 'Т'] + quit_list):
        if go_on == out_com:
            exit = True
    clean_screen()
    return exit


# the body of the program

quit_list = ['q', 'й', 'Q', 'Й', 'quit', 'exit', 'make', 'clear']
our_Library = Library()

while True:

    # Main menu
    print("""Main menu:
    What do you want to do?
Enter - to continue
    a - to add a new book
    c - to change the status of the book
    d - to delete the book
    f - to finding the book
    s - to showing all books
    q - to exiting the program"""
    )
    
    # Waiting for a command from the user
    if main_menu_options(quit_list):
        break

    # Additional menu
    if additionnal_menu_options(quit_list):
        break