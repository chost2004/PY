'''
Complete the function scramble(str1, str2) that returns true
if a portion of str1 characters can be rearranged to match str2,
otherwise returns false.

Notes:
Only lower case letters will be used (a-z). No punctuation or
digits will be included.
Performance needs to be considered
Input strings s1 and s2 are null terminated.

Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False

'''
def scramble(text1, text2):
    for i in text2:
        if text2.count(i) > text1.count(i):
            return False
    return True
text1 = input('Введите строку 1: ')
text2 = input('Введите строку 2: ')
print (scramble(text1, text2))
            
            
    
