N = int(input("Введите число элементов массива "))
A = []
X = int(input("Введите число, наличие которого хотите узнать в массиве "))
count = 0
for i in range(1,N+1):
    A.append(i)
for num in A:
    if num == X:
        count += 1
print(A)
print(count)