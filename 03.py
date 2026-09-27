# Arithmetic product and conditional logic

def arithmetic_product(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return  num1 + num2

print(arithmetic_product(10, 30))