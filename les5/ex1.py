def countFactorial(n):
    if n == 1:
        return n
    else:
        return n * countFactorial(n - 1)

def countTriangle(n):
    if n == 1:
        return n
    else:
        return n + countTriangle(n - 1)