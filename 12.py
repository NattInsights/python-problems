# palindrome number checker without converting to a string
def is_palindrome(number):
    reverse_num = 0
    digit = 0
    new_num = number
    while new_num % 10 > 0:
        digit = new_num % 10
        reverse_num = (reverse_num * 10) + digit
        new_num //= 10
    return reverse_num == number

print(is_palindrome(350))

# fixed, but probably not optimal