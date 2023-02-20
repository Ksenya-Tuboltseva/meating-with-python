S = 24
if S % 6 == 0:
    Petya = S / 6
    Serezha = Petya
    Katya = (Petya + Serezha) * 2
    print(int(Petya))
    print(int(Katya))
    print(int(Serezha))
else:
    print("Невозможно решить задачу, используя введенное число")