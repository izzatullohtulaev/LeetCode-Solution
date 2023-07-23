def generate(numRows: int):
    superarray = []
    subarray = [1]
    old_subarray = [1]
    if numRows == 1:
        print(subarray)
    else:
        for row in range(1, numRows+1):
            subarray = []
            for i in range(row):
                if i == 0:
                    subarray.append(old_subarray[0]+0)
                elif i == row-1:
                    subarray.append(old_subarray[-1]+0)
                else:
                    subarray.append(old_subarray[i]+old_subarray[i-1])
            # print(subarray)
            superarray.append(subarray)
            old_subarray = subarray
    return superarray


print(generate(5))

# rows = int(input("The number of the rows: "))
