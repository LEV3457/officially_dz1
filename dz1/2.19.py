a = int(input("Введите число:"))
b = a % 100 // 10 + a % 10 + a // 1000 + a // 1000 % 10
c = (a % 100 // 10) * (a % 10) * (a // 1000) * (a // 1000 % 10)
print(b, c)