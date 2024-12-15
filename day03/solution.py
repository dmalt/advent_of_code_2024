import re

mul = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")


def exec_muls(text: str) -> int:
    return sum(int(m[0]) * int(m[1]) for m in re.findall(mul, text))


with open("input.txt") as f:
    text = f.read()


answer1 = exec_muls(text)
answer2 = sum(exec_muls(x.split("don't()")[0]) for x in text.split("do()"))

print(f"{answer1=}")
print(f"{answer2=}")
