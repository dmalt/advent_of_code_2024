from itertools import pairwise


def check_nums(nums):
    is_inc = (nums[1] - nums[0]) > 0
    
    for x, y in pairwise(nums):
        if x == y:
            return False
        if x > y and is_inc:
            return False
        if x < y and not is_inc:
            return False
        if abs(x - y) > 3:
            return False
    return True

sum = 0
with open("input1.txt") as f:
    for line in f:
        nums = list(map(int, line.split()))
        if check_nums(nums):
            print("Safe: ", nums)
            sum += 1
        else:
            print("Unsafe: ", nums)


print(sum)
