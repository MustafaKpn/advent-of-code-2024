import re

with open("input.txt", 'r') as f:
    read = f.read()

all_does = re.sub(r"don't\(\).*?do", "do", read, flags=re.DOTALL)
all_does = re.sub(r"don't\(\).*?do", "do", all_does, flags=re.DOTALL)
all_does = re.sub(r"don't\(\).*?do", "do", all_does, flags=re.DOTALL)
no_dont = re.sub(r"don't\(\).*", "", all_does, flags=re.DOTALL)

muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", no_dont, flags=re.DOTALL)
sums = 0

for i in muls:
    new_value = i.replace('mul(', '').replace(')', '').split(',')
    sums += (int(new_value[0]) * int(new_value[1]))

