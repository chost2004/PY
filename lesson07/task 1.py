import math
n = str(math.factorial(int(input('Введите число: '))))

res = 0;
i = len(n) - 1
while i >=0:
    if n[i] == '0':
        res += 1
    elif n[i] != '0':
        break
    i -= 1
    
 

#Выводим количество нулей в конце n!

 

print(n,res);
