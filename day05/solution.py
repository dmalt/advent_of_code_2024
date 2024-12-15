from collections import defaultdict

all_rules = defaultdict(set)
with open("input_large_rules.txt") as f:
    for line in f:
        page_earlier, page_later = line.strip().split("|")
        all_rules[page_earlier].add(page_later)

updates = []
with open("input_large_updates.txt") as f:
    for line in f:
        updates.append(line.strip().split(","))


def get_relevant_rules(update: list[str]) -> dict[str, set[str]]:
    relevant_rules = defaultdict(set)

    for page_earlier in update:
        for page_later in all_rules[page_earlier]:
            if page_later not in update:
                continue
            relevant_rules[page_earlier].add(page_later)
    return relevant_rules


def is_good_update(update: list[str], rules: dict[str, set[str]]) -> bool:
    for i, c in enumerate(update):
        if c not in rules:
            continue
        for rule_page in rules[c]:
            if rule_page not in update[i + 1 :]:
                return False
    return True


def _topo_sort(start, edges, seen, order) -> None:
    if start in seen:
        return
    seen.add(start)

    children = edges.get(start, [])

    for c in children:
        _topo_sort(c, edges, seen, order)

    order.append(start)


def topo_sort(rules: dict[str, set[str]]) -> list[str]:
    order = []
    seen = set()

    for r in rules:
        _topo_sort(r, rules, seen, order)
    return list(reversed(order))


answer1 = 0
answer2 = 0
for o in updates:
    rules = get_relevant_rules(o)
    if is_good_update(o, rules):
        answer1 += int(o[len(o) // 2])
    else:
        # print(f"{rules=}")
        # print(f"{o=}")
        # print(f"{topo_sort(rules)=}")
        o_sort = topo_sort(rules)
        assert len(o_sort) == len(o)
        answer2 += int(o_sort[len(o) // 2])


print(f"{answer1=}")
print(f"{answer2=}")
