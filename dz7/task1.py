'''
Task 1:
Move the first letter of each word to the end of it,
then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
pigIt('Hello world !');     // elloHay orldway !
'''
def pigIt(pigs):
    output = []
    for pig in pigs:
        pig = list(pig) 
        for i in range(len(pig)):
            if pig[i].isalpha():
                break
            else:
                i+=1
        for p in range(len(pig)-1,-1,-1):
            if pig[p].isalpha():
                break
        if p == 0:
            pig = ''.join(pig)
            output.append(pig)
        else:    
            pig.insert(p+1,'ay')
            pig.insert(p+1, pig[i])
            del pig[i]
            pig = ''.join(pig)
    #        print (pig)
            output.append(pig)
    print (' '.join(output))
text = (input('Enter text: ')).split()
pigIt(text)
