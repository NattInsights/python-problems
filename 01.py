# Sum of numbers from 1 to n
def sum_of_numbers(n):
    if n < 1:
        return 0
    return n + sum_of_numbers(n - 1)

print(sum_of_numbers(5))

# recursive solution above, similar to factorial