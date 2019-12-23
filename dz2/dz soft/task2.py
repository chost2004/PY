n = int(input("число"))
n1 = n % 10
n2 = n // 10 % 10
n3 = n // 100 % 10
n4 = n // 1000 % 10
S = n1 * n2 * n3 * n4

revers = n1 * 1000 + n2 * 100 + n3 * 10 + n4

N = [n1,n2,n3,n4] 
z = 1 
while z < len(N):
 for i in range(len(N)-z):
  if N[i] > N[i+1]:
    N[i],N[i+1] = N[i+1],N[i]
 z += 1
ordered = N[0] * 1000 + N[1] * 100 + N[2] * 10 + N[3]
     
print(S, revers, ordered)
