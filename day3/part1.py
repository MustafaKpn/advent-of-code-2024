import re



with open("input.txt", 'r') as f:
    read = f.read()



match = re.findall(r'mul\(\d{1,3},\d{1,3}\)', read)

for index, value in enumerate(match):
    new_value = value.replace('mul(', '')
    new_value = new_value.replace(')', '').split(',')
    match[index] = new_value


sum = 0

for i in match:
    sum += int(i[0]) * int(i[1])


