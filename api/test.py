

count = dict()

n = int(input())
for _ in range(n):
    word = input()
    count[word] = count.get(word, 0) + 1
    if count[word] > 1:
        new_word = word + (f'({count[word] - 1})' if count[word] > 1 else "")
        if new_word != word:
            count[new_word] = count.get(new_word, 0) + 1
        print(new_word)
    else:
        print(word)
    