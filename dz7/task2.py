'''
Write an algorithm that takes an array and
moves all of the zeros to the end, preserving
the order of the other elements.

moveZeros([false,1,0,1,2,0,1,3,"a"]) //
returns[false,1,1,2,1,3,"a",0,0]

'''
def moveZeros(text):
    for i in range(len(text)-1,-1,-1):
        if text[i] == '0':
            text.append(text.pop(i))
    return text
text = input('Введите текст').split(',')
print (','.join(moveZeros(text)))
            
            
    
