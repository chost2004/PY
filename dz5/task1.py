'''
Про инков
'''
s = [c for c in input('Введите: ')]
s.append('.')

i = 0
knot = 0
prepend = ['(', ')', '+', '-', '/', '*']
p = []
while i <= len(s)- 2:
    if s[i] in prepend :
        p.append(s[i])
    elif (s[i] == '@') and (s[i+1] == '@'):
        knot += 1
    elif (s[i] == '@') and (s[i+1] != '@'):
        knot += 1
        p.append(knot)
        knot = 0
    elif (s[i] == '~') and (s[i-1] == '~'):
        p.append(0)
    i += 1
#print (p)
p1 = []
for num in p:
    p1.append(str(num))
primer = ''.join(p1)
otvet = eval(primer)
otvet = int(otvet)
print (otvet)
otvet = str(otvet)
#print (type(otvet))
quipu = []
i = 0
while i <= (len (otvet) -1):
    if (int(otvet[i]) in range (1, 10)) and (i < (len (otvet) -1)):
        q = '@' * int(otvet [i])
        quipu.append(q)
        quipu.append('~')
    elif (int(otvet[i]) in range (1, 10)) and (i == (len (otvet) -1)):
        q = '@' * int(otvet [i])
        quipu.append(q)
    elif int(otvet[i]) == 0:
        quipu.append('~')
    i+=1
print (''.join(quipu))
        
        

