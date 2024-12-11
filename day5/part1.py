with open("input.txt", 'r') as f:
    read = f.readlines()

rules = []
pages = []
for i in read:
    if i != '\n' and ',' not in i:
        rule = i.strip()
        rule = rule.split('|')
        rule1 = int(rule[0])
        rule2 = int(rule[1])
        rules.append((rule1, rule2))

    elif ',' in i:
        pages.append([int(j) for j in i.strip().split(',')])

def check_rule(num_test, test_list, rules):
    for i in test_list:
        for j in rules:
            if num_test == j[1] and i == j[0]:
                return False
    return True


correct_rules = []
for x in pages:
    
    for i, v in enumerate(x):
        test_list = x[i:]
        status = check_rule(v, test_list, rules)
        if not status:
            break
    if status:
        correct_rules.append(x)

middle_values = [i[int(len(i)/2)] for i in correct_rules]
print(sum(middle_values))