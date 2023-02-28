N = int(input("Введите число элементов массива "))
A = []
X = int(input("Введите число, близкое к которому хотите найти в массиве "))
for i in range(1,N+1):
    A.append(i)
print(A)
if X in A:
    print(f"Заданное число {X} есть в массиве")
elif X < 1:
    print("Самое близкое к искомому - число 1 в массиве")
else:
    print(f"Самое близкое к искомому - число {N} в массиве")

#or

from random import randint
lst = [randint(-10,10) for _ in range(int(input("Задайте количество элементов массива ")))]
print(lst)
k = int(input("Задайте число, котрое хотите найти "))
difference = abs(lst[0] - k)
target = lst[0]
for i in range(1, len(lst)):
    diff = abs(lst[i] - k)
    difference = diff
    target = lst[i]
print(f"Самый близкий к искомому числу {k} в массиве - {target}")