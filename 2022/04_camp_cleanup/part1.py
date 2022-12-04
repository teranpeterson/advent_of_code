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
        if (elf1_start <= elf2_start and elf1_end >= elf2_end) or (elf2_start <= elf1_start and elf2_end >= elf1_end):
            sum += 1
    print(sum)