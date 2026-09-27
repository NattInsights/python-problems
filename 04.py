# Cumulative sum of range

def cum_sum(n):
    total = 0
    for i in range(0, n + 1):
        total += i
    return total

print(cum_sum((10)))