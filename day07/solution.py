# from operator


def reduce(numbers, operators):
    if len(numbers) == 1:
        return numbers[0]
    if operators[0] == "*":
        numbers[1] *= numbers[0]
    else:
        assert operators[0] == "+"
        numbers[1] += numbers[0]
    return reduce(numbers[1:], operators[1:])


def reduce2(numbers, operators):
    if len(numbers) == 1:
        return numbers[0]
    if operators[0] == "*":
        numbers[1] *= numbers[0]
    elif operators[0] == "+":
        numbers[1] += numbers[0]
    else:
        assert operators[0] == "|"
        n = len(str(numbers[1]))
        numbers[1] += numbers[0] * 10**n
    return reduce2(numbers[1:], operators[1:])


def make_operators(n):
    if n == 1:
        yield "+"
        yield "*"
        return
    for op in make_operators(n - 1):
        yield op + "+"
        yield op + "*"


def make_operators2(n):
    if n == 1:
        yield "+"
        yield "*"
        yield "|"
        return
    for op in make_operators2(n - 1):
        yield op + "+"
        yield op + "*"
        yield op + "|"


def check(ans, numbers):
    n = len(numbers) - 1
    for op_seq in make_operators(n):
        if ans == reduce(numbers.copy(), op_seq):
            return True
    return False


def check2(ans, numbers):
    n = len(numbers) - 1
    for op_seq in make_operators2(n):
        if ans == reduce2(numbers.copy(), op_seq):
            return True
    return False


answer1 = 0
with open("input_small.txt") as f:
# with open("input_large.txt") as f:
    for line in f:
        first, rest = line.strip().split(":")
        first = int(first)
        rest = list(map(lambda x: int(x), rest.split()))
        if check(first, rest):
            answer1 += first
print(f"{answer1=}")

answer2 = 0
# with open("input_small.txt") as f:
with open("input_large.txt") as f:
    for line in f:
        first, rest = line.strip().split(":")
        first = int(first)
        rest = list(map(lambda x: int(x), rest.split()))
        if check2(first, rest):
            answer2 += first
print(f"{answer2=}")
