# фамилия | имя | номер телефона | должность | компания
'''
Телефонный справочник. Добавление контакта, удаление контакта,
редактирование контакта. Поиск по имени-фамилии, поиск по номеру,
поиск по частично набранному номеру
'''


class Contact:
    '''Work with contact'''
    def __init__(self, surname, name, phone_numbers, position, company):
        self.surname = surname
        self.name = name
        self.phone_numbers = phone_numbers
        self.phone_numbers_aray = phone_numbers.strip(',')
        self.position = position
        self.company = company
        self.contact = [self.surname, self.name, self.phone_numbers, self.position, self.company]
   
    def __str__(self):
        return f"{self.surname} {self.name} {self.phone_numbers} {self.position} {self.company}"
    
    def search(self, text):
        '''search text in contact'''
        for cell in self.contact:
            if text in cell:
                return True

    def modify(self,choice):
        ''' modify contact'''
        if choice == 1:
            self.surname = input('enter surname: ')
        elif choice == 2:
            self.name = input('enter name: ')
        elif choice == 3:
            self.phone_numbers = input('enter phone: ')
            self.phone_numbers_aray = phone_numbers.strip(',')
        elif choice == 4:
            self.position = input('enter position: ')
        elif choice == 5:
            self.company = input('enter company: ')
    
    def print(self):
        '''print contact'''
        print(f"{self.surname} {self.name} {self.phone_numbers} {self.position} {self.company}")

    def save(self):
        '''for save file'''
        return f"{self.surname} | {self.name} | {self.phone_numbers} | {self.position} | {self.company}\n"
        
class PhoneBook:
    '''work with phone book'''
    def __init__(self, file):
        self.file = file
        self.array = []
        with open(self.file, 'r') as phone_book:
            for line in phone_book:
                self.array.append(Contact(*line.strip().split(' | ')))
                
    @property
    def len(self):
        ''' quantity contacts'''
        return len(self.array)
    
    def print(self):
        '''print all contacts'''
        for n in self.array:
            print(n)
            
    def add(self,new_contact):
        '''add contact'''
        self.array.append(Contact(*new_contact))
        
    def remove(self,n):
        '''remove contact'''
        del self.array[n]
        
    def search(self, text):
        '''search and print contact'''
        for n in self.array:
            if n.search(text):
                n.print()
            
    def sorted(self):
        '''sort phonebook'''
        self.array = sorted(self.array, key = lambda d : d.surname + d.name)

    def save(self):
        '''save file'''
        with open(self.file, 'w') as phone_book:
            pass
        with open(self.file, 'a') as phone_book:
            temp_text = ''
            for contact in self.array:
                temp_text = temp_text + contact.save()
            phone_book.write(temp_text)
            

class Menu:
    '''menu for work with phonebook'''
    def __init__(self,file):
        self.phone_book = PhoneBook(file)

    def main(self):
        '''main menu'''
        while True:
            print('1 - print all contacts')
            print('2 - search contact')
            print('3 - add contact')
            print('4 - remove contact')
            print('5 - modify contact')
            print('6 - quit')
            choice = input('What we do now? ')
            if choice == '1':
                self.phone_book.print()
            elif choice == '2':
                text = input('enter text for search')
                self.phone_book.search(text)
            elif choice == '3':
                self.add_menu()
            elif choice == '4':
                contact_number = int(input('what number of contact you want delete? ')) - 1
                self.phone_book.remove(contact_number)
                self.phone_book.save()
            elif choice == '5':
                contact_number = int(input('what number of contact you want modify? ')) - 1
                self.modify_menu(contact_number)
                self.phone_book.save()
            elif choice == '6':
                break

    def add_menu(self):
        ''' use for add new contact'''
        new_contact = []
        new_contact.append(input('enter surname: '))
        new_contact.append(input('enter name: '))
        new_contact.append(input('enter phone numbers separate ",": '))
        new_contact.append(input('enter position: '))
        new_contact.append(input('enter company: '))
        self.phone_book.add(new_contact)
        self.phone_book.sorted()
        self.phone_book.save()

    def modify_menu(self, contact_number):
        '''use for modify contact'''
        print(self.phone_book.array[contact_number])
        print('what do you want modify?')
        print('1 surname')
        print('2 name')
        print('3 phone')
        print('4 position')
        print('5 company')
        choice = int(input())
        self.phone_book.array[contact_number].modify(choice)
        self.phone_book.sorted()
        self.phone_book.save()
                       
        
    
menu = Menu('phonebook.txt')
menu.main()
