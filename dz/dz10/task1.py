def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0,5) + 1):
        if number % i == 0:
            return False
        return True
def prime_number_in_range(start, end):
    print(f"от {start} до {end}")
    for number in range(start, end + 1):
        if is_prime(number):
            print(number, end=" ")
            print()
num0 = int(input("Введите число"))
num1 = int(input("Введите число"))
prime_number_in_range(num0, num1)


