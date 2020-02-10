from . import phonebook

class Menu:
    '''menu for work with phonebook'''
    def __init__(self,file):
        self.phone_book = phonebook.PhoneBook(file)

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
