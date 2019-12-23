A1 = int(input('Стоимость песка первого вида:'))
A2 = int(input('Стоимость песка второго вида:'))
A3 = int(input('Стоимость песка третьего вида:'))
B1 = int(input('Вместимость первой емкости:'))
B2 = int(input('Вместимость второй емкости:'))
B3 = int(input('Вместимость третьей емкости:'))
if A1 <= 0 or A2 <= 0 or A3 <= 0 or A1 > 100 or A2 > 100 or A3 > 100 \
or B1 <= 0 or B2 <= 0 or B3 <= 0 or B1 > 100 or B2 > 100 or B3 > 100:
    print("Входные данные не верны")
else:
    A = [A1,A2,A3] 
    n = 1 
    while n < len(A):
     for i in range(len(A)-n):
          if A[i] > A[i+1]:
               A[i],A[i+1] = A[i+1],A[i]
     n += 1

    B = [A1,A2,A3] 
    n = 1 
    while n < len(B):
     for i in range(len(B)-n):
          if B[i] > B[i+1]:
               B[i],B[i+1] = B[i+1],B[i]
     n += 1

    S = B[2] * A[2] + B[1] * A[1] + B[0] * A[0]


    print('Прибыль:',S)
input ('Нажмите Enter для выхода')
