def function_find_len(x):
    return len(x)


def count_most_used_char(word):
    # intentionally unoptimized function
    total = {}

    for c in word:
        if c not in total.keys():
            total[c] = 1
        else:
            total[c] += 1

    max = total[word[0]]

    for c in word:
        if total[c] > max:
            max = total[c]

    return max
