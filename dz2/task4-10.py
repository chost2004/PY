'''
10. Запросить дату (день, месяц, год) и вывести следующую за ней дату.
Учтите возможность перехода на следующий месяц, год, а также високосный год
'''

from datetime import datetime, timedelta

YYYY = int(input ('Введите год YYYY'))
MM = int (input ('Введите месяц MM'))
DD = int (input ('Введите дату DD'))
a = datetime(YYYY, MM, DD)
b = timedelta(days=1)
print (str(a))
print (str(a+b))

