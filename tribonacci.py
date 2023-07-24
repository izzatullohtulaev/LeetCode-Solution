def tribonacci(n):
    array = [0, 1, 1]
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    for t in range(3, n+1):
        array.append(array[t-1]+array[t-2]+array[t-3])
    return array[-1]