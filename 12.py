# palindrome number checker without converting to a string
def is_palindrome(number):
    reverse_num = 0
    if number > 0:
        reverse_num.append(number % 10)
        number //= 10

    if reverse_num == number:
        return True
    return False 

print(is_palindrome(121))

#logic for building up a new number is still compromised
#yet to figure out maths