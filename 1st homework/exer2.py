n = input("Введите трехзначное число: ")
if len(n) == 3:
    summ = int(n[0]) + int(n[1]) + int(n[2])
    print(summ)
else:
    print("Неверный формат числа")