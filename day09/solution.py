from itertools import chain


def is_even(i):
    if i % 2:
        return False
    return True


def decompress(compressed):
    decompressed = []
    free_inds = []
    data_inds = []
    data_id = 0
    for i, num in enumerate(compressed):
        if is_even(i):
            new_data = [data_id] * num
            data_inds.append((len(decompressed), len(decompressed) + len(new_data)))
            data_id += 1
        else:
            new_data = ["."] * num
            free_inds.append((len(decompressed), len(decompressed) + len(new_data)))
        decompressed.extend(new_data)
    return decompressed, free_inds, data_inds


def print_swap(line, i, j):
    print("".join(map(str, line)))
    underline = [" "] * len(line)
    underline[i] = "^"
    underline[j] = "^"
    print("".join(map(str, underline)))


def unwrap(inds: list[tuple[int, int]]) -> list[int]:
    return list(chain.from_iterable(range(a, b) for a, b in inds))


def defragment1(decompressed, free_inds, data_inds):
    for i, j in zip(reversed(unwrap(data_inds)), unwrap(free_inds)):
        # print_swap(decompressed, i, j)
        if j >= i:
            break
        decompressed[i], decompressed[j] = decompressed[j], decompressed[i]


def find_free_segment(free_inds: list[tuple[int, int]], data_lo: int, data_hi: int):
    # if not free_inds:
    #     return False
    # if free_inds[0][0] > data_lo:
    #     return False

    len_data = data_hi - data_lo
    for i, (free_lo, free_hi) in enumerate(free_inds):
        len_free = free_hi - free_lo
        if free_lo > data_lo:
            return None
        if len_data <= len_free:
            return i, free_lo, free_hi


def defragment2(decompressed, free_inds, data_inds):
    for i, j in reversed(data_inds):
        # print(f"{i=}, {j=}, data={''.join(map(str, decompressed[i:j]))}")
        # print(free_inds)
        if (res := find_free_segment(free_inds, i, j)) is None:
            # print("not found")
            continue
        # print("".join(map(str, decompressed)), end=" -> ")
        k, free_lo, free_hi = res
        free_inds[k] = (free_lo + j - i, free_hi)
        decompressed[free_lo : free_lo + j - i] = decompressed[i:j]
        decompressed[i:j] = ["."] * (j - i)
        # print("".join(map(str, decompressed)))


def compute_hash(nums):
    hash = 0
    for i, num in enumerate(nums):
        if num == ".":
            continue
        hash += i * num
    return hash


with open("input_large.txt") as f:
    compressed = list(map(int, f.readline().strip()))

decompressed, free_inds, data_inds = decompress(compressed)
# print(f"{''.join(map(str, decompressed))}, {free_inds=}, {data_inds=}")
decompressed1 = decompressed.copy()
decompressed2 = decompressed.copy()
defragment1(decompressed1, free_inds.copy(), data_inds.copy())
defragment2(decompressed2, free_inds.copy(), data_inds.copy())

# print("".join(map(str, decompressed1)))
answer1 = compute_hash(decompressed1)
print(f"{answer1=}")

# print("".join(map(str, decompressed2)))
answer2 = compute_hash(decompressed2)
print(f"{answer2=}")
