n = int(input("Введите значение n "))
m = int(input("Введите значение m "))
set1 = set()
set2 = set()
for i in range(1,n+1):
    i = int(input())
    set1.add(i)
print(set1)
for i in range(1,m+1):
    i = int(input())
    set2.add(i)
print(set2)
inner = set1.intersection(set2)
print(sorted(inner))