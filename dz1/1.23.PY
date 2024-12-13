a = int(input("Введите четырехзначное число:"))
if a > 999:
    c = a // 100 % 10
    d = a // 1000 % 10

    print(c, d)
else: 
    print("False")