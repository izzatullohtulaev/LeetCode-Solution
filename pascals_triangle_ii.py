def getRow(rows: int):
    subarray = []
    old_subarray = [1]
    if rows==0:
        subarray.append(1)
        return subarray
    for row in range(1, rows+1):
        subarray = []
        for i in range(row):
            if i == 0:
                subarray.append(old_subarray[0])
            elif i == row-1:
                subarray.append(old_subarray[-1])
            else:
                subarray.append(old_subarray[i]+old_subarray[i-1])
    old_subarray = subarray[:]
    # subarray = []
    print(old_subarray)
