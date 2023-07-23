def generate(numRows: int):
    superarray = [[1]]
    subarray = [1]
    superarray += subarray
    if numRows == 1:
        return superarray


print(generate(1))