# String indexing and even slicing

string = input("Enter a word: ")

for i in range(len(string)):
    if i % 2 == 0:
        print(string[i])