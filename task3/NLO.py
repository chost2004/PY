L=int(input("Введите количество панелей:"))
if (L<0 or L>100) and L.is_integer():
    print("Количество панелей не верное")
else:
    A=int(input("Введите высоту панели:"))
    if A<0 or A>100:
        print("Высота указана не верно")
    else:
        B=int(input("Введите ширину панели:"))
        if B<0 or B>100:
            print("Ширина указана не верно")
        else:
            C=L*B*2*A
            print(C,"нанограм")
input('Press ENTER to exit')
 
