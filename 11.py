# flitering lists with conditional logic
def div_5(numbers):
    valid = list()
    for i in numbers:
        if i % 5 == 0:
            valid.append(i)
    return valid

print(div_5([5, 12, 18, 25, 50]))