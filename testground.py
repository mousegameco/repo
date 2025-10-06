
input = [2, 3, 5, 4]
output = []
# x in range of 4
for x in range(len(input)):
    # y in range of 4 (differrent from x)
    for y in range(x + 1, len(input)):
        #if two numbers added = 8 therefore their position were shown
        if int(input[x]) + int(input[y]) == 8:
            output.extend([x, y])

print(output)
