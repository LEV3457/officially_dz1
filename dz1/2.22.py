a = int(input("Введите трехзначное число:"))
if a > 99:
    c = a // 100
    d = a // 10 % 10
    print(c, d)
else: 
    print("False")