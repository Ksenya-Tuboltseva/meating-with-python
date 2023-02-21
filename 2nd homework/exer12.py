S = int(input("Зачение суммы "))
P = int(input("Зачение произведения "))
def searcing_numbers(sum,product):
    for i in range(sum):
        for j in range(product):
            if sum == i + j and product == i * j:
                return f"Загаданные значения равны {i} и {j}"
    return "Такой комбинации чисел не существует"
print(searcing_numbers(S,P))