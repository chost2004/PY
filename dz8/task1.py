a = 2
b = 100
c = str (bin(b))
#print (c)
count = -3
for d in c: count += 1 
#print (count)
def fun(a,b,count):
    dva = 2**count
    if dva in range (a, b + 1):
        return dva
    for d in range (a, b + 1) :
#        print (d, count)
        if d > dva: 
          if not d / dva - int(d / dva):
            return d
    count -= 1
    return fun (a,b,count)
print (fun (a,b,count))
