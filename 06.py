# String slicing and substring removal

def remove_chars(word, n):
    word = word[n:]
    return word

print(remove_chars("pynative", 2))