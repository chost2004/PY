# Login
from datetime import datetime
now = datetime.now()
print (now)
login = input ('login: ') + '.txt'
password = input ('pass: ')
while 1:
    if password  != '1234':
        password = input ('not valid, pass: ')
    else :
        break
text = str(now) + ' ' + input ('input text: ') + '\n'
with open (login, 'a') as f:
    f.write(text)
    
