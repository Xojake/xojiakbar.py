while True:
    son = int(input("Qaysi sonni kvarati kerak: "))
    print(f"{son} - kvadrati {son**2}")

    savol = input("Yana davom etamizmi(yes/no): ")
    if savol == "yes":
        continue
    elif savol == "no":
        print("Tugadi")
        break
    else:
        print("Yes yoki No kiriting! ")







son = 1
while son<=5: 
    print(son, end=' ') 
    son += 1
    print('The end')






while True:
    yil = int(input("Tug'ilgan yilingizni kiriting: "))
    print(f"Sizning yoshingiz {2024-yil} ")

    savoll = input("Yana davom etamizmi(exit): ")
    if savoll == "exit":
        print("Tugadi")
        break










parol = 123

sorash = int(input("Parol kiriting: "))


while True:
    if parol == sorash:
        print("Xush kelibsiz! ")
        break
    
    if sorash != parol:
        print("xato")
        sorash2 = int(input("Qaytatdan kiriting: "))
        if parol != sorash2:
            print("Xato")
        elif parol == sorash2:
            print("Xush kelibsiz")
            break
    sorash3 = int(input("Yana qaytatdan kiriting: "))
    if parol == sorash3:
        print("Xush kelibsiz! ")
    elif parol != sorash3:
        while True:
            print("Yeding")







parol = 123
urinish = 0


while True:
    sorash = int(input(f" {urinish+1} - chi urunish Parol kiriting: "))
    if parol == sorash:
        print("Xush kelibsiz! ")
        break
    elif sorash != parol:
        urinish += 1
        if urinish == 3:
            while True:
                print("Yeding")