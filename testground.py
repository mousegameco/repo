
input = [2, 3, 5, 4]
output = []
for x in range(len(input)):
    for y in range(x + 1, len(input)):
        if int(input[x]) + int(input[y]) == 8:
            output.extend([x, y])

print(output)
