


with open('input.txt', 'r') as f:
    lines = f.readlines()

left_list = []
right_list = []

for i in lines:
    line_split = i.strip().split(' ')
    if len(line_split) > 1:
        left_list.append(int(line_split[0]))
        right_list.append(int(line_split[3]))


left_list_sorted = sorted(left_list)
right_list_sorted = sorted(right_list)



distances = []
for i in range(len(left_list)):
    distances.append(abs(left_list_sorted[i] - right_list_sorted[i]))





