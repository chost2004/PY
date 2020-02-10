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
        
