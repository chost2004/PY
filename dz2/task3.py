N = int(input('Введите № билета:'))
if N < 0 or N >= 10**6:
    print("Входные данные не верны")
else:
    N1 = N % 10 
    N2 = N // 10 % 10
    N3 = N // 100 % 10
    N4 = N // 1000 % 10
    N5 = N // 10000 % 10
    N6 = N // 100000 % 10
    if N1 + N2 +N3  == N4 + N5 + N6:
        print ('yes')
    else:
        print('No')
input ('Нажмите Enter для выхода')
