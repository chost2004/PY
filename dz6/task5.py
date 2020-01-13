'''
Task 5:

Создать массив, описывающий чек в магазине.
Каждый элемент массива состоит из названия товара,
количества и цены за единицу товара. Написать следующие функции. 

1. Распечатка чека на экран. 

2. Подсчет общей суммы покупки. 

3. Получение самой дорогой покупки в чеке. 

4. Подсчет средней стоимости одного товара в чеке.


'''
shopping_list = [['Сметана', 2, 2.05], ['Сок', 4, 3.10], ['Молоко', 1, 22.20], ['Напиток', 1, 3.30]]

def print_shop():
    for i in shopping_list:
        print (i,'\n')
    
def summ():
    summa = 0
    for i in shopping_list:
        summa += (i[1]*i[2])
    return summa
        


def max_shop():
    maxbuy = 0
    for i in shopping_list:
        if (i[1]*i[2])>maxbuy:
            maxbuy = (i[1]*i[2])
            z = i[0]
    return z

def average():
    summa = 0
    z = 0
    for i in shopping_list:
        z += 1
        summa += i[2]
    return summa / z

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

print_shop()
print('-----------------------')
print("Сумма:", summ())
print('-----------------------')
print("Самая дорогая покупка :",max_shop())
print('-----------------------')
print("Средняя стоимость одного товара :",toFixed(average(),2))

