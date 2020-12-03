def pairs(ar):
    if len(ar) % 2 == 1:
        ar = ar[0:-1]
    count = 0
    for i in range(0, len(ar), 2):
        first = ar[i]
        second = ar[i+1]
        if first + 1 == second or first - 1 == second:
            count += 1
    return count
