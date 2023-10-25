def head(filepath, num_lines):
    with open(filepath, "r", encoding="UTF-8") as f:
        for line in f:
            yield line
            num_lines -= 1
            if num_lines == 0:
                break

filename = "C:/Users/SamuraJ/Documents/Codes/Python/Generators/war.txt"
for line in head(filename, 100):
    print(line, sep="", end="")