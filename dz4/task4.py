'''
 Bears are either 'B' (male) or '8' (female),
 Bears must be together in male/female pairs 'B8' or '8B',
 Mating pairs must involve two distinct bears each
 ('B8B' may look fun, but does not count as two pairs).


'''
n = input('Введите значения через запятую: ').split(',')
if len(n) > 1:
    s = str(n[1])
    l = int(n[0])
else:
    s = str(n[0])
    l = 'NO'
    
i = 0
pair = []
count = 0
while i < (len(s)-1):
    if s[i] == 'B' and s[i+1] == '8':
        pair.append('B8')
        count +=1
        i+=1
    elif s[i] == '8' and s[i+1] == 'B':
        pair.append('8B')
        count +=1
        i+=1
    i +=1
if l == 'NO':
    result = ''
elif l <= count:
    result = 'True'
else :
    result = 'False' 
print (result, ''.join(pair))
    


