from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations, product

arr = []
with open("input_large.txt") as f:
    for line in f:
        arr.append(list(line.strip()))


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, num: int) -> "Point":
        return Point(self.x * num, self.y * num)

    def __rmul__(self, num: int) -> "Point":
        return Point(self.x * num, self.y * num)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def is_in_box(self, m: int, n: int) -> bool:
        if self.x < 0 or self.y < 0:
            return False
        if self.x >= m or self.y >= n:
            return False
        return True


def get_locations_per_type(arr) -> dict[str, list[Point]]:
    locations = defaultdict(list)
    m, n = len(arr), len(arr[0])

    for i, j in product(range(m), range(n)):
        if (c := arr[i][j]) == ".":
            continue
        locations[c].append(Point(i, j))
    return locations


def compute_antinodes(locs: list[Point], m: int, n: int) -> set[Point]:
    antinodes = set()
    for a, b in combinations(locs, 2):
        # if a == b:
        #     continue
        node1, node2 = 2 * a - b, 2 * b - a
        if node1.is_in_box(m, n):
            antinodes.add(node1)
        if node2.is_in_box(m, n):
            antinodes.add(node2)
    return antinodes


def compute_antinodes_multi(locs: list[Point], m: int, n: int) -> set[Point]:
    antinodes = set()
    for a, b in combinations(locs, 2):
        delta = a - b
        node = a
        while node.is_in_box(m, n):
            antinodes.add(node)
            node += delta
        node = b
        while node.is_in_box(m, n):
            antinodes.add(node)
            node -= delta

    return antinodes


ll = get_locations_per_type(arr)
m, n = len(arr), len(arr[0])

answer1 = 0
antinodes_all = set()
antinodes_all_multi = set()
for _, locs in ll.items():
    antinodes = compute_antinodes(locs, m, n)
    antinodes_multi = compute_antinodes_multi(locs, m, n)
    for a in antinodes:
        arr[a.x][a.y] = "#"
    antinodes_all.update(antinodes)
    antinodes_all_multi.update(antinodes_multi)
answer1 = len(antinodes_all)
answer2 = len(antinodes_all_multi)

print(f"{answer1=}")
print(f"{answer2=}")

# for line in arr:
#     print("".join(line))
