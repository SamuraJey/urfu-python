def head(filepath, num_lines):
    with open(filepath, "r", encoding="UTF-8") as f:
        for line in f:
            yield line
            num_lines -= 1
            if num_lines == 0:
                break


filename = "Second Lection/war.txt"
for line in head(filename, 10):
    print(line, sep="", end="")
