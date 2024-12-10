import re
with open("input.txt", "r") as f:
    read = f.readlines()


lines = []
vertical_lines = []
vertical_results = 0
horizontal_results = 0
diagonal_results = 0
line_length = 140

for line in read:
    if len(line) > 1:
        lines.append(line.strip())
        line = line.strip()
        horizontal_results += len(re.findall(r"XMAS", line))
        horizontal_results += len(re.findall(r"XMAS", line[::-1]))\
        

for j in range(140):
    new_vertical = ''
    for i, v in enumerate(lines):
        new_vertical += v[j]
    vertical_lines.append(new_vertical)

for line in vertical_lines:
    vertical_results += len(re.findall(r"XMAS", line))
    vertical_results += len(re.findall(r"XMAS", line[::-1]))


diagonal_lines = [[j for j in i] for i in lines]

def diagonals(matrix):
    n = len(matrix)
    diagonals = []  
    for p in range(2*n-1):
        diagonals.append([matrix[p-q][q] for q in range(max(0, p - n + 1), min(p, n - 1) + 1)])
        diagonals.append([matrix[n-p+q-1][q] for q in range(max(0, p - n + 1), min(p, n - 1) + 1)])
    return diagonals


diagonal_lines = diagonals(diagonal_lines)
for i in diagonal_lines:
    diagonal_results += (len(re.findall("XMAS", "".join(i))))
    diagonal_results += (len(re.findall("XMAS", "".join(i[::-1]))))
    

print(horizontal_results + vertical_results + diagonal_results)