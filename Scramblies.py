from collections import Counter
def scramble(s1, s2):
    letters = Counter(s1)
    word = Counter(s2)
    return all(word[i] <= letters[i] for i in word)