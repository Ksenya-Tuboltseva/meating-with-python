N = int(input("Введите количество кустов "))
lst = []
for i in range(1,N+1):
    lst.append(int(input()))
print(lst)
maximus = 0
for i in range(0,N-1):
    if i == 0:
        if lst[i] + lst[i+1] + lst[-1] > maximus:
            maximus = lst[i] + lst[i+1] + lst[-1]
    elif i == len(lst):
        if lst[i] + lst[0] + lst[1] > maximus:
            maximus = lst[i] + lst[0] + lst[1]
    else:
        if lst[i] + lst[i-1] + lst[i+1] > maximus:
            maximus = lst[i] + lst[i-1] + lst[i+1]
print(maximus)