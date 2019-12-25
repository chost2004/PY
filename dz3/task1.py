'''
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive
alphabetic characters and numeric digits that occur more than once in the input string.
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
'''

s = input('Введите текст:').lower()
i = 0
n = 0
while i < len(s):
    if n < s.count(s[i]):
        n = s.count(s[i])
    i+=1
print (n)
    


