monkeys = {
    "monkey0": {
        "count": 0,
        "items": [52, 78, 79, 63, 51, 94],
        "op": lambda old: old * 13,
        "divisor": 5,
        "true": "monkey1",
        "false": "monkey6",
    },
    "monkey1": {
        "count": 0,
        "items": [77, 94, 70, 83, 53],
        "op": lambda old: old + 3,
        "divisor": 7,
        "true": "monkey5",
        "false": "monkey3",
    },
    "monkey2": {
        "count": 0,
        "items": [98, 50, 76],
        "op": lambda old: old * old,
        "divisor": 13,
        "true": "monkey0",
        "false": "monkey6",
    },
    "monkey3": {
        "count": 0,
        "items": [92, 91, 61, 75, 99, 63, 84, 69],
        "op": lambda old: old + 5,
        "divisor": 11,
        "true": "monkey5",
        "false": "monkey7",
    },
    "monkey4": {
        "count": 0,
        "items": [51, 53, 83, 52],
        "op": lambda old: old + 7,
        "divisor": 3,
        "true": "monkey2",
        "false": "monkey0",
    },
    "monkey5": {
        "count": 0,
        "items": [76, 76],
        "op": lambda old: old + 4,
        "divisor": 2,
        "true": "monkey4",
        "false": "monkey7",
    },
    "monkey6": {
        "count": 0,
        "items": [75, 59, 93, 69, 76, 96, 65],
        "op": lambda old: old * 19,
        "divisor": 17,
        "true": "monkey1",
        "false": "monkey3",
    },
    "monkey7": {
        "count": 0,
        "items": [89],
        "op": lambda old: old + 2,
        "divisor": 19,
        "true": "monkey2",
        "false": "monkey4",
    },
}

for i in range(20):
    for j in range(8):
        monkey = monkeys[f"monkey{j}"]
        for idx, item in enumerate(monkey["items"]):
            monkey["count"] += 1
            new = monkey["op"](item)
            new = int(new / 3)
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