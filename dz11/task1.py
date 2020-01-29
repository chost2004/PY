'''
Реализовать класс, описывающий геометрическую фигуру со свойствами и методами: 
- get-свойство для получения названия фигуры; 
- метод для вывода информации о фигуре (стороны и их длина); 
- метод для вычисления площади фигуры; 
- метод для вычисления периметра фигуры. 

Реализуйте классы-наследники: квадрат, прямоугольник и треугольник.
Переопределите методы вывода и вычислений в классах-наследниках. 
Создайте массив с различными фигурами и выведите информацию о каждой фигуре,
включая площадь и периметр.
'''
class Polygons:
    def __init__(self, *side_length):
        self.side_length = side_length
    @property
    def prop(self):
        return str(len(self.side_length))+'-angle'
    def side(self):
        return self.side_length
    def perimeter(self):
        return sum(self.side_length)

figure = Polygons(3,5,6,7,7)
print(figure.prop)
for i, side in enumerate(figure.side()):
    print(f'{i + 1}я сторона {side}')
print(f'Периметр {figure.perimeter()}')

class Triangles(Polygons):
    def __init__(self, *side_length):
        self.side_length = side_length
    @property
    def prop(self):
        return 'Треугольник'
    @property
    def p(self):
        return self.perimeter() / 2
    def S(self):
        return (self.p * (self.p - self.side_length[0]) *
                         (self.p - self.side_length[1]) *
                         (self.p - self.side_length[2]))**0.5

trianle = Triangles(3,5,6)
print(trianle.prop)
for i, side in enumerate(trianle.side()):
    print(f'{i + 1}я сторона {side}')
print(f'Периметр {trianle.perimeter()}')
print(f'Площадь треугольника {trianle.S():.2f}')    

class Square(Polygons):
    def __init__(self, side_length):
        self.side_length = []
        for i in range (4):
            self.side_length.append(side_length)
    @property
    def prop(self):
        return 'Квадрат'
    def S(self):
        return self.side_length[0] ** 2

square = Square(3)
print(square.prop)
for i, side in enumerate(square.side()):
    print(f'{i + 1}я сторона {side}')
print(f'Периметр {square.perimeter()}')
print(f'Площадь квадрата {square.S():.2f}')

class Rectangles(Polygons):
    def __init__(self, *side_length):
        self.side_length = []
        for i in range (2):
            self.side_length.append(side_length[0])
            self.side_length.append(side_length[1])
    @property
    def prop(self):
        return 'Прямоугольник'
    def S(self):
        return self.side_length[0] * self.side_length[1]

rectangle = Rectangles(3,4)
print(rectangle.prop)
for i, side in enumerate(rectangle.side()):
    print(f'{i + 1}я сторона {side}')
print(f'Периметр {rectangle.perimeter()}')
print(f'Площадь прямоугольника {rectangle.S():.2f}')

        
    
