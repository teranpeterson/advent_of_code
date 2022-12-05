with open("input.txt", "r") as file:
    crates = {
        's1': ['H', 'R', 'B', 'D', 'Z', 'F', 'L', 'S'],
        's2': ['T', 'B', 'M', 'Z', 'R'],
        's3': ['Z', 'L', 'C', 'H', 'N', 'S'],
        's4': ['S', 'C', 'F', 'J'],
        's5': ['P', 'G', 'H', 'W', 'R', 'Z', 'B'],
        's6': ['V', 'J', 'Z', 'G', 'D', 'N', 'M', 'T'],
        's7': ['G', 'L', 'N', 'W', 'F', 'S', 'P', 'Q'],
        's8': ['M', 'Z', 'R'],
        's9': ['M', 'C', 'L', 'G', 'V', 'R', 'T'],
    }

    for line in file:
        line = line.strip()
        line = line.split(' ')
        for i in range(int(line[1])):
            if len(crates[f's{line[3]}']) > 0:
                x = crates[f's{line[3]}'].pop()
                crates[f's{line[5]}'].append(x)
    
    print(crates)
    for k, v in crates.items():
        print(v[-1], end='')
    print()