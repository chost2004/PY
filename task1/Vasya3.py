#Task1 Vasya 2
#Profit 'P' for 'n' string
p=50
n=100
#Penalty 'a' for being late 'l'
a=20
b=3
#second - total string 'N' + total late 'L' = total profit 'P'
print('enter total late')
L=input()
print('enter total string')
N=input()
P=int(N)//int(n)*int(p)-int(L)//int(b)*int(a)
print(P)
