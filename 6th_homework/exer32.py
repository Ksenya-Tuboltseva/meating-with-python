min = int(input("Введите минимальное значение "))
max = int(input("Введите максимальное значение "))
import random
lst = random.sample(range(1,100),10)
print(lst)
for i in range(0,len(lst)):
    if lst[i] > min and lst[i] < max:
        print(i)