def countSingleSum(a, b):
    if a == 0:
        return b
    return countSingleSum(a - 1, b + 1)