'''
parse molekula
'''
import re
t=input('Введите формулу: ').replace("[", '(').replace("]", ')').replace("{", '(').replace("}", ')')
d={}
p,q="(\([^\(\)]*\))(\d*)","([A-Z][a-z]*)(\d*)"
for i in re.findall(q,t):
    t = t.replace(i[0]+i[1],i[0]*(1 if i[1]==''else int(i[1])))
r=re.findall(p,t)
while len(r)>0:
    t=t.replace(r[0][0]+r[0][1],r[0][0][1:-1]*(1 if r[0][1]==''else int(r[0][1])))
    r=re.findall(p,t)
for i in re.findall(q[:-5], t):
    d[i]=d[i]+1 if i in d else 1
for i in d:print(i+': '+str(d[i]))
            
            
    
