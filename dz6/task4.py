'''
Создать массив «Список покупок». Каждый элемент массива является объектом,
который содержит название продукта, необходимое количество и куплен или нет.
Написать несколько функций для работы с таким массивом.

  1. Вывод всего списка на экран таким образом,
  чтобы сначала шли некупленные продукты, а потом – купленные.

  2. Добавление покупки в список. Учтите, что при добавлении
  покупки с уже существующим в списке продуктом, необходимо
  увеличивать количество в существующей покупке, а не добавлять новую.

  3. Покупка продукта. Функция принимает название продукта и отмечает
  его как купленный.

'''
shopping_list = [['Сметана', 'нужен', 2], ['Сок', 'куплен', 3], ['Молоко', 'нужен', 1], ['Напиток', 'куплен', 3]]

def print_shop():
    for i in shopping_list:
        if i[1] == 'нужен':
            print (i,'\n')
    for i in shopping_list:
        if i[1] == 'куплен':
            print (i,'\n')

def search(item):
    for i in range (len(shopping_list)):
        if shopping_list[i][0] == item:
            return i+1
    else:
        return 0

def shop(item, quantity = 1):
    global shopping_list
    i = search(item)
    if i:
        if shopping_list[i-1][1] == 'куплен':
            shopping_list[i-1][2] = quantity
            shopping_list[i-1][1] = 'нужен'
        else:
            shopping_list[i-1][2] += quantity
    else:
         shopping_list.append([item, 'нужен', quantity])

def buy(item):
    global shopping_list
    i = search(item)
    if i :
        shopping_list[i-1][1] = 'куплен'
    else:
        print ('Такой продукт не требуется')
print_shop()
print ('--------------------')
shop ('tomat')
shop ('Напиток' ,3)        
print_shop()
print ('--------------------')
buy ('Напиток')        
print_shop()
