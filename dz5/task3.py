string = 'Yesterday, we bumped into Laura. It had to happen, but you can\'t deny the timing couldn\'t be worse. The "mission" to try and seduce her was a complete failure last month. By the way, she still has the ring I gave her. Anyhow, it hasn\'t been a pleasurable experience to go through it. I wanted to feel done with it first.'
key = string.split('. ')[0]
text = string.split('. ')
key = key.split()
for i in range (len(key)):
    key[i] = key[i].strip(',').strip('"')
    
#print (key)
n = len (key)
#print (n)
dic = []
for i in range (1,n+1):
    word = (text[i]).split()[len(key[i-1])-1]
    word = word.strip(',').strip('"')
    dic.append(word)
dic[0] = dic [0].title()    
print (' '.join(dic), '.', sep = '')

