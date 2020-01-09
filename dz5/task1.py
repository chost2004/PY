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
    elif (s[i] == '~') and (s[i+1] == '~'):
        space = 0
        for z in range (i, len(s)-1):
            if s[z] == '~':
                space += 1
            else:
                i = z - 1
                space = space // 2 + 1
                print (space)
                for c in range (space):
                    p.append(0)
                break
    i += 1
#print (p)
p1 = []
for num in p:
    p1.append(str(num))
primer = ''.join(p1)
otvet = eval(primer)
print (otvet)
otvet = str(otvet)
print (type(otvet))
quipu = []
for num in otvet:
    if int(num) in range (1, 10):
        q = '@' * int(num)
        print (q)
        


     

'''
@@@@@@@
i = 1
n = 0
while i <= s:
    i (s % i) == 0:
        n = n + i 
    i+=1
print (n)
    
'''

