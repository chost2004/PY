'''
Написать конвертор валют. Пользователь вводит количество USD,
выбирает, в какую валюту хочет перевести: EUR, UAH или AZN,
и получает в ответ соответствующую сумму.

'''
USD = int(input('USD '))
Valuta = int(input ("Выберите 1-EUR, 2-UAH, 3-AZN "))
if Valuta == 1:
    S = USD * 0,9
    print(S)
elif Valuta == 2:
    S = USD * 24
    print(S)
elif Valuta == 3:
    S = USD / 2
    print(S)
else :
    print('fault')
