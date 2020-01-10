n = int(input('Enter digit: '))

#Генерация всех разбиений.
#a = [1,1,1,1,1,1,1,1]
a=[]
for i in range (n):
    a.append(1)
#print (a)
#print (n)
maximum = 0
maxfun = []
while 1:
#	Печать и выход. Print end exit.
#        print(a)
        if (a[0] == n):
            break
#	Элемент в нулевом индексе нашего динамического массива на текущий момент.
        first_elem = a[0]
	
#	Размер массива на текущий момент. 
        c = len(a) - 1
        i = 0
        min_elem = 0
        while (i != len(a) - 1):
		
#	Найдем элемент меньше первого.
                if a[i] < first_elem:
                    first_elem = a[i]
                    min_elem = i
			
                i+=1
		
		
#	Перенос элемента  "1".
        a[min_elem]+= 1
        a[c]-= 1
        if a[c] == 0:
            del(a[c])

#       ищем произведение
        product = 1
        print (a)
        for i in range (len (a)):
            product *= a[i]
        print(product)

#       Ищем максимальное
        if maximum < product:
            maximum = int (product)
            maxfun.clear()
            maxfun.append(list(a))
        elif maximum == product:
            maxfun.append(list(a))

maxfun.reverse()
print ('Решение:', maxfun, maximum)
        
            

