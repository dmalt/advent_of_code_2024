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


def is_x_mas(text, i, j):
    square_cut = text[i - 1 : i + 2, j - 1 : j + 2]
    c1 = square_cut.diagonal()
    if "MAS" not in ("".join(c1), "".join(reversed(c1))):
        return False
    c2 = np.flip(square_cut, axis=0).diagonal()
    if "MAS" not in ("".join(c2), "".join(reversed(c2))):
        return False
    return True


answer1 = 0
answer2 = 0
for i, j in product(range(text_arr.shape[0]), range(text_arr.shape[1])):
    if text_arr[i, j] == "X":
        answer1 += count_xmas(text_arr, i, j)
    if text_arr[i, j] == "A":
        answer2 += is_x_mas(text_arr, i, j)

print(f"{answer1=}") 
print(f"{answer2=}") 
