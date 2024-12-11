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
            data_inds.extend(
                range(len(decompressed), len(decompressed) + len(new_data))
            )
            data_id += 1
        else:
            new_data = ["."] * num
            free_inds.extend(
                range(len(decompressed), len(decompressed) + len(new_data))
            )
        decompressed.extend(new_data)
    return decompressed, free_inds, data_inds

def print_swap(line, i, j):
    print(''.join(map(str, line)))
    underline = [" "] * len(line)
    underline[i] = "^"
    underline[j] = "^"
    print(''.join(map(str, underline)))


def defragment(decompressed, free_inds, data_inds):
    for i, j in zip(reversed(data_inds), free_inds):
        # print_swap(decompressed, i, j)
        if j >= i:
            break
        decompressed[i], decompressed[j] = decompressed[j], decompressed[i]


def compute_hash(nums):
    hash = 0
    for i, num in enumerate(nums):
        if num == ".":
            return hash
        hash += i * num
    return hash



with open("input_large.txt") as f:
    compressed = list(map(int, f.readline().strip()))

decompressed, free_inds, data_inds = decompress(compressed)
print(f"{''.join(map(str, decompressed))}, {free_inds=}, {data_inds=}")
defragment(decompressed, free_inds, data_inds)

print(''.join(map(str, decompressed)))
answer1 = compute_hash(decompressed)
print(f"{answer1=}") 
