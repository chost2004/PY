from . import contact

class PhoneBook:
    '''work with phone book'''
    def __init__(self, file):
        self.file = file
        self.array = []
        with open(self.file, 'r') as phone_book:
            for line in phone_book:
                self.array.append(contact.Contact(*line.strip().split(' | ')))
                
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
        self.array.append(contact.Contact(*new_contact))
        
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
            
