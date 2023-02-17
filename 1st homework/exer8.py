n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
k = int(input("Введите число k: "))
if k%n == 0 or k%m == 0:
    print(f"Можно отломить {k} долек")
else:
    print(f"Нельзя отломить {k} долек")