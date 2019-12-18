#Task1 Vasya 2
#Profit 'P' for 'n' string
p=50
n=100
#Penalty 'a' for being late 'l'
a=20
b=3
#second - total string 'N' + total profit 'P' = total late 'L'
print('enter total profit')
P=input()
print('enter total string')
N=input()
L=(int(N)//int(n)*int(p)-int(P))//int(a)*int(b)+int(b)-1
if L < 0:
    print('Вася не опаздывай тебе еще пахать и пахать')
else:
    print(L)


