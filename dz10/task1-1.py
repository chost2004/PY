'''
    Реализовать класс, описывающий простой маркер.
В классе должны быть следующие компоненты: 
- поле, которое хранит цвет маркера; 
- поле, которое хранит количество чернил в маркере (в процентах); 
- метод для печати (метод принимает строку и выводит текст
    соответствующим цветом; текст выводится до тех пор,
    пока в маркере есть чернила; один не пробельный символ –
    это 0,5% чернил в маркере). 
    Реализовать класс, описывающий заправляющийся маркер,
унаследовав его от простого маркера и добавив метод для
заправки маркера. Продемонстрировать работу написанных методов


'''
import colorama
from colorama import Fore, Style
colorama.init()


class Marker():
    def __init__(self, color = 'black', ink_quantity = 100):
        self.color = color
        self.ink_quantity = float(ink_quantity)
    ink_consumption = 0.5
    def print_method(self):
        text = input('Enter text for print: ')
        eval('print(Fore.' + self.color.upper() + ')')
        for i in text:
            if i == ' ':
                print(i, end = '')
            elif self.ink_quantity >= 0.5:
                print(i, end = '')
                self.ink_quantity -= self.ink_consumption
            else:
                print(Style.RESET_ALL)
                print('\nno ink!!!')
                break
        print('\n')
        print(Style.RESET_ALL)

color = input('Enter color of marker: ')
ink_quantity = float(input('Enter ink_quantity in %: '))
marker_1 = Marker(color, ink_quantity)

while True:
    a = input('Please select 1 to print or 2 for quit: ')
    if a == '1' :
        marker_1.print_method()
    elif a == '2':
        break
    
