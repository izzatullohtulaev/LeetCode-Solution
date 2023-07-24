def minimumTotal(triangle):
    ans = 0
    for row in triangle:
        min_val = min(row)
        ans += min_val
    return ans
    