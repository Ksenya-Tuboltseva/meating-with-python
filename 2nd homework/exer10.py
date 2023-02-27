n = 10
coin_list = []
import random
for i in range(n):
    coin_list.append(random.randint(0,1))
print(coin_list)
count_0 = 0 #счетчик нулевых значений (решка)
count_1 = 0 #счетчик единичных значений (орел)
for coin in coin_list:
    if coin == 0:
        count_0 += 1
    else:
        count_1 += 1
if count_0 > count_1:
    print(f"Нужно перевернуть {count_1} монет")
else:
    print(f"Нужно перевернуть {count_0} монет")