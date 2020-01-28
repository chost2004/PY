'''
Реализовать класс Employee, описывающий работника,
и создать массив работников банка. 
Реализовать класс EmpTable для генерации кода таблицы
со списком работников банка. 
Массив работников необходимо передавать через конструктор,
а получать код с помощью метода getCodel(). 
Создать объект класса EmpTable и вывести в консоль
результат работы метода getCode()
'''
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
rab1 = Employee('Petrov', 50)
rab2 = Employee('Ivanov', 45)
rab3 = Employee('Sidorov', 20)
rabs = [rab1, rab2, rab3]

class EmpTable:
    def __init__(self, rabs):
        self.rabs = rabs
    def getCode(self):
        for rab in rabs:
            print (rab.name, rab.age)

tabl = EmpTable(rabs)
tabl.getCode()
    
    
