# Factorial of a number n
def factorial(n):
    res = 1
    if n == 0:
        return res
    return n * factorial(n - 1)

print(factorial(5))