'''
Запросить у пользователя год и проверить, високосный он или нет.
Високосный год либо кратен 400, либо кратен 4 и при этом не кратен 100.
'''
n = int(input('Введите год: '))
a = "нет"
if (n % 400 == 0) or ((n % 4) == 0 and (n % 100) > 0):
    a = "да"
print(a)
input ('Нажмите Enter для выхода')
