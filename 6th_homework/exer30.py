first = int(input("Введите первый элемент "))
diff = int(input("Введите разность "))
n = int(input("Введите количество элементов "))
lst =[first]
for i in range(1,n):
    lst.append(first + i*diff)
print(lst)