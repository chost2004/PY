#/*Генерация всех разбиений.   Generate all partitions.*/
a = [1,1,1,1,1,1,1]
n = sum(a)
print (a)
print (n)

while 1:
#	/*Печать и выход. Print end exit.*/
        print(a)
        if (a[0] == n):
            break
#	/*Элемент в нулевом индексе нашего динамического массива на текущий момент.
        first_elem = a[0]
	
#	/*Размер массива на текущий момент. Length of an array*/
        c = len(a) - 1
        i = 0
        min_elem = 0
        while (i != len(a) - 1):
		
#		/*Найдем элемент меньше первого. Here we search min. element.*/
                if (a[i] < first_elem)and (a[i] != 0):
                    first_elem = a[i]
                    min_elem = i
			
                i+=1
		
		
#	/*Перенос элемента  "1". Here we transfer "1". */
        a[min_elem]+= 1
        a[c]-= 1
        if a[c] == 0:
            del(a[c])
#        print (a)
'''	
	/*Обрежем массив и найдем сумму его элементов. We cut the array
	* and count the sum of elements.*/
	array_splice($a, $min_elem + 1);
	$array_sum = array_sum($a);
	
	/*Добавим в массив единицы заново с учетом суммы.
	Here we add 1 (fill)  to the array
	( taking into account the sum ).*/
	for ($j = 0; $j != $n - $array_sum; $j++) $a[] = 1;
	
	/*Обнулим переменную. Unset min_elem.*/
	unset($min_elem);
	}
	'''
