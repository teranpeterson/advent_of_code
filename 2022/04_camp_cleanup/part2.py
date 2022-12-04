with open("input.txt", "r") as file:
    sum = 0
    for line in file:
        line = line.strip()
        elf1, elf2 = line.split(",")
        elf1_start, elf1_end = elf1.split("-")
        elf2_start, elf2_end = elf2.split("-")
        elf1_start = int(elf1_start)
        elf1_end = int(elf1_end)
        elf2_start = int(elf2_start)
        elf2_end = int(elf2_end)
        if (elf1_end >= elf2_start and elf1_start <= elf2_end) or (elf2_end >= elf1_start and elf2_start <= elf1_end):
            sum += 1
    print(sum)


# .234.....  2-4
# .....678.  6-8

# .23......  2-3
# ...45....  4-5

# ....567..  5-7
# ......789  7-9

# .2345678.  2-8
# ..34567..  3-7

# .....6...  6-6
# ...456...  4-6

# .23456...  2-6
# ...45678.  4-8

# .....345. 
# ..23.....