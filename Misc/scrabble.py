import itertools

points = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
}


def scrabble():
    dictionary = open("dictionary.txt", "r")
    word = dictionary.readlines()
    dictionary.close()

    scores = {}

    for line in word:
        line = line.rstrip("\n")
        total = 0
        for letter in line:
            letter = letter.lower()
            total += points.get(letter, 0)
            scores.update({line: total})

    full_dict = {
        key: value
        for key, value in sorted(scores.items(), key=lambda word: word[1], reverse=True)
    }

    chunks = 4
    chunkdict = {}
    chunksize = len(full_dict) // chunks
    items = iter(full_dict.items())

    for i in range(chunks - 1):
        chunkdict["chunk_{}".format(i)] = dict(itertools.islice(items, chunksize))
    else:
        chunkdict["chunk_{}".format(chunks - 1)] = dict(items)

    return chunkdict


def testscrabble(word):
    total = 0
    for letter in word:
        letter = letter.lower()
        total += points.get(letter, 0)
    return total


# chunks = scrabble()
# print(chunks["chunk_0"])
# print(chunks["chunk_1"])
# print(chunks["chunk_2"])
# print(chunks["chunk_3"])
