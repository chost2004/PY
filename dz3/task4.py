'''
Simple, given a string of words, return the length of the shortest word(s).
'''

s = input('Введите текст:')
s = s.split()
i=0
while i < len(s):
    if i == 0:
        n = len(s[i])
    elif len(s[i]) < n:
        n = len(s[i])
    i+=1
print (n)
