# multiplication for 12 to 20 times tables

def times(numbers):
    for i in numbers:
        for j in range(1, 13):
            print(i * j, end=" ")
        print("\n")
    return None

times(range(12, 21))

# not great implementation, not reusable also thus far
# formatting is better now