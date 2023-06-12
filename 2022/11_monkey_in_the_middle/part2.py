monkeys = {
    "monkey0": {
        "count": 0,
        "items": [79, 98],
        "op": lambda old: old * 19,
        "divisor": 23,
        "true": "monkey2",
        "false": "monkey3",
    },
    "monkey1": {
        "count": 0,
        "items": [54, 65, 75, 74],
        "op": lambda old: old + 6,
        "divisor": 19,
        "true": "monkey2",
        "false": "monkey0",
    },
    "monkey2": {
        "count": 0,
        "items": [79, 60, 97],
        "op": lambda old: old * old,
        "divisor": 13,
        "true": "monkey1",
        "false": "monkey3",
    },
    "monkey3": {
        "count": 0,
        "items": [74],
        "op": lambda old: old + 3,
        "divisor": 17,
        "true": "monkey0",
        "false": "monkey1",
    },
}

for i in range(10000):
    for j in range(4):
        monkey = monkeys[f"monkey{j}"]
        for idx, item in enumerate(monkey["items"]):
            monkey["count"] += 1
            new = monkey["op"](item)
            if new % monkey["divisor"] == 0:
                monkeys[monkey["true"]]["items"].append(new)
            else:
                monkeys[monkey["false"]]["items"].append(new)
        monkey["items"].clear()

counts = []
for k, v in monkeys.items():
    counts.append(v["count"])
counts.sort(reverse=True)
print(counts[0] * counts[1])