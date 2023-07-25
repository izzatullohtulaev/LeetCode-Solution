def climbStairs(n: int) -> int:
    arr = [1, 1]
    if n == 1:
        return 1
    for num in range(2, n+1):
        arr.append(arr[num-1]+arr[num-2])
    return arr

