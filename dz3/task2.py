'''
In DNA strings, symbols "A" and "T" are complements of each other,
as "C" and "G". You have function with one side of the DNA
(string, except for Haskell); you need to get the other complementary side.
DNA strand is never empty or there is no DNA at all (again, except for Haskell).
'''

s = input('Введите текст:').upper()
if s.count('A') == 0 and s.count('C') == 0 and s.count('T') == 0 and s.count('G') == 0 :
    print ('DNA strand is never empty or there is no DNA')
else:
    trans1 = 'ATGC'
    trans2 = 'TACG'
    trans3 = s.maketrans(trans1,trans2)
    print (s.translate(trans3))
    


