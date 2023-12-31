import re
data = open("data.txt").readlines()
dirs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
adjacent = []

for line in range(len(data)):
    x = 0
    while x < len(data[line]):
        char = data[line][x]
        if char.isdigit():
            checked = False
            number = re.split(r'[^\d]+', data[line][x:])[0]
            for i, digit in enumerate(number):
                for dir in dirs:
                    row, col = line + dir[0], x + dir[1] + i
                    if 0 <= row < len(data) and 0 <= col < len(data[row]) and data[row][col] != "." and not data[row][col].isdigit() and data[row][col] != "\n":
                        adjacent.append(int(number))
                        checked = True
                if checked:
                    break  
            x += len(number)
        else:
            x += 1

print(sum(adjacent))
