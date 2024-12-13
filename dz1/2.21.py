a = int(input("Введите двухзначное число:"))
if a > 9:
    c = a // 10
    d = a % 10
    print(c, d)
else: 
    print("False")