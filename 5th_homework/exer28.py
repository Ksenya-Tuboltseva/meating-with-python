A = int(input("Введите число "))
B = int(input("Введите второе число "))
def sum(a,b):
    if b == 0:
        return a
    return sum(a+1,b-1)

print(sum(A,B))