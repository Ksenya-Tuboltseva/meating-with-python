A = int(input("Введите число "))
B = int(input("Введите степень числа "))
def num_degree(a,b):
    if b == 1:
        return a
    return a * num_degree(a,b-1)

print(num_degree(A,B))