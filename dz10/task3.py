'''
Реализовать класс, описывающий окружность. В классе должны быть следующие компоненты: 
- поле, хранящее радиус окружности; 
- get-свойство, возвращающее радиус окружности; 
- set-свойство, устанавливающее радиус окружности; 
- get-свойство, возвращающее диаметр окружности; 
- метод, вычисляющий площадь окружности; 
- метод, вычисляющий длину окружности. 

Продемонстрировать работу свойств и методов
'''

class Circle:
    def __init__(self,r=10):
        self.r = int(r)
    def get_r(self):
        print('r = ', self.r, '\n')
    def get_d(self):
        print('d = ', self.r * 2, '\n')
    def set_r(self):
        self.r = int(input('Enter r: '))
    def get_lench(self):
        print('l = ', 6.28 * self.r, '\n')
    def get_square(self):
        print('S = ', 3.14 * self.r ** 2, '\n')

circle = Circle()
while True:
    a = int(input('1 - get r\n2 - set r\n3 - get d\n4 - get lench\n5 - get square\n6 - exit\n'))
    if a == 1:
        circle.get_r()
    elif a == 2:
        circle.set_r()
    elif a == 3:
        circle.get_d()
    elif a == 4:
        circle.get_lench()
    elif a == 5:
        circle.get_square()
    elif a == 6:
        break

    
    
