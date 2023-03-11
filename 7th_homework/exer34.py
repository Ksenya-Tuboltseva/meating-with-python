poem_str = "пара-ра-рам рам-пам-папам па-ра-па-да"
poem_lst = poem_str.split()
rhyme = list(map(lambda x: x.count('а'), poem_lst))
if len(set(rhyme)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")