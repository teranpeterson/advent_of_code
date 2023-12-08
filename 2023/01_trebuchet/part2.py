with open('input.txt', 'r') as file:
    res = 0
    for line in file:
        i = 0
        tokens = []
        for i in range(len(line)):
            c = line[i]
            if c.isnumeric():
                tokens.append(c)
            elif i + 3 < len(line) and line[i:i+3] == 'one':
                tokens.append('1')
            elif i + 3 < len(line) and line[i:i+3] == 'two':
                tokens.append('2')
            elif i + 5 < len(line) and line[i:i+5] == 'three':
                tokens.append('3')
            elif i + 4 < len(line) and line[i:i+4] == 'four':
                tokens.append('4')
            elif i + 4 < len(line) and line[i:i+4] == 'five':
                tokens.append('5')
            elif i + 3 < len(line) and line[i:i+3] == 'six':
                tokens.append('6')
            elif i + 5 < len(line) and line[i:i+5] == 'seven':
                tokens.append('7')
            elif i + 5 < len(line) and line[i:i+5] == 'eight':
                tokens.append('8')
            elif i + 4 < len(line) and line[i:i+4] == 'nine':
                tokens.append('9')
        res += int(tokens[0] + tokens[-1])
    print(res)