# factorial with a loop 
def factorial(number):
    res = 1
    while number >= 1:
        res *= number
        number -= 1
    return res

print(factorial(5))