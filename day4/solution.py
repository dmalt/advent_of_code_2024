from itertools import product

import numpy as np

with open("input.txt") as f:
    text = list(map(lambda x: list(x.strip()), f.readlines()))

text_arr = np.array(text)


def count_xmas(text, i, j):
    candidates = [
        text[i, j : j + 4],
        reversed(text[i, j - 3 : j + 1]),
        text[i : i + 4, j],
        reversed(text[i - 3 : i + 1, j]),
        text[i : i + 4, j : j + 4].diagonal(),
        reversed(text[i - 3 : i + 1, j - 3 : j + 1].diagonal()),
        np.flip(text[i - 3 : i + 1, j : j + 4], axis=0).diagonal(),
        reversed(np.flip(text[i : i + 4, j - 3 : j + 1], axis=0).diagonal()),
    ]
    res = sum("".join(c) == "XMAS" for c in candidates)
    return res

answer1 = 0
for i, j in product(range(text_arr.shape[0]), range(text_arr.shape[1])):
    if text_arr[i, j] == "X":
        answer1 += count_xmas(text_arr, i, j)
