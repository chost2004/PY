W = float(input('Введите ширину:'))
L = float(input('Введите длину:'))
H = float(input('Введите высоту:'))
if L <= 0 or W <= 0 or H <= 0 or L > 1000 or W > 1000 or H > 1000:
    print("Входные данные не верны")
else:
    S = (W + L) * H * 2
    n=0
    if (S % 16) > 0:
        n=1
    N = S//16+n
    print('Необходимо банок краски:', int(N))
