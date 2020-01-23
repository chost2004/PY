# Library
def read_fun():
    with open('books.txt', 'r') as books:
        library = []
        for book in books:
           library.append(book.strip('\n').split('*'))
        return library


def print_fun(library):
    print ('-'*100)
    for i in library:
        print('{0:4}|{1:30}|{2:15}|{3:20}|{4:5}|{5:12}|{6:8}'.format(*i))
        if i[0]=='id':
            print ('-'*100)
    print ('-'*100)

def gen_id(library):
    gen = []
    for i in library:
        if i[0] != 'id':
            gen.append(int(i[0]))
    gen = max(gen)+1
    return gen

def input_book():
    global library
    book = []
    book.append (str(gen_id(library)))
    book.append (input('Enter name of book: \n'))
    while check_name(book[1]):
        book[1] = input('This name of book alredy exist, enter other one: \n')
    book.append (input('Enter author: \n'))
    book.append (input('Enter genre: \n'))
    book.append (input('Enter publishing year: \n'))
    book.append (input('Enter publishing house: \n'))
    book.append (input('Enter price: \n'))
    return book

def check_name(name):
    global library
    for i in library:
        if name == i [1]:
            return True
    return False

def write_fun(book):
    with open ('books.txt', 'a') as f:
        f.write('*'.join(book)+'\n')
    print ('The book is added')


while 1:
    a = input('Please choice:\n1 - print all books\n2 - add book\n3 - quite\n')
    if a == '1':
        library = read_fun()
        print_fun(library)
    elif a == '2':
        library = read_fun()
        new_book = input_book()
        write_fun(new_book)
    elif a == '3':
        break

