from typing import Counter


seen = Counter()

def is_even(x: int) -> bool:
    return x % 2 == 0


def step(num: str) -> tuple[str, ...]:
    seen[num] += 1
    if num == "0":
        return ("1",)
    if is_even(len(num)):
        ind = int(len(num) / 2)
        return num[:ind], str(int(num[ind:]))
    return (str(int(num) * 2024), )

def step_all(stones: list[str]):
    res = []
    for s in stones:
        res.extend(step(s))
    return res

cache = {}

def dfs(stone: str, depth: int, max_depth: int):
    if (max_depth - depth, stone) in cache:
        return cache[(max_depth - depth, stone)]
    if depth == max_depth:
        return 1
    cache[(max_depth - depth, stone)] = sum(dfs(s, depth + 1, max_depth) for s in step(stone))
    return cache[(max_depth - depth, stone)]


with open("input_large.txt") as f:
    stones = f.readline().strip().split()



answer1 = 0
answer2 = 0
print(stones)
for start_stone in stones:
    res1 = dfs(start_stone, 0, 25)
    res2 = dfs(start_stone, 0, 75)
    print(f"done {start_stone}")
    print(f"{len(cache)=}") 
    answer1 += res1
    answer2 += res2
print(f"{answer1=}") 
print(f"{answer2=}") 
