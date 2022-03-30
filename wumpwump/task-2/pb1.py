def mystery(lst):
    if len(lst) == 0:
        return
    first = lst[0]
    for i in range(len(lst)-1):
        lst[i] = lst[i + 1]
    lst[-1] = first


print(mystery([1]))