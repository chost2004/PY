#Task1 Vasya 1
#Profit 'P' for 'n' string
p=50
n=100
#Penalty 'a' for being late 'l'
a=20
b=3
#first - total profit 'P' + total late 'L' = total string 'N'
print('enter total profit')
P=input()
print('enter total late')
L=input()
if (int(P)+int(L)//b*int(a))//int(p) > 0:
   C=100
else:
   C=0
N=(int(P)+int(L)//b*int(a))//int(p)*int(n)+int(C)
print(N)


