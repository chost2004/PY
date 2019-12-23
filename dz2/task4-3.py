
n = int(input('Введите трехзначное число: '))
n1 = n%10
n2 = n//10%10
n3 = n//100%10
A = 'есть' if n1 == n2 or n1 == n3 or n2 == n3 else 'нет'
print(A)
input ('Нажмите Enter для выхода')
