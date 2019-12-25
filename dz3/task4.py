'''
our task is to sort a given string.
Each word in the string will contain a single number.
This number is the position the word should have in the result.
4of Fo1r pe6ople g3ood th5e the2

'''

s = input('Введите текст:')
s = s.split()
n = list(s)
i=0
while i < len(s):
    if s[i].count('1'):
        n[0] = s[i]
    elif s[i].count('2'):
        n[1] = s[i]
    elif s[i].count('3'):
        n[2] = s[i]
    elif s[i].count('4'):
        n[3] = s[i]
    elif s[i].count('5'):
        n[4] = s[i]
    elif s[i].count('6'):
        n[5] = s[i]
    elif s[i].count('7'):
        n[6] = s[i]
    elif s[i].count('8'):
        n[7] = s[i]
    elif s[i].count('9'):
        n[8] = s[i]
    i+=1
n=' '.join(n)
print (n)
