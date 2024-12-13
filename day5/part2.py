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


def check_single_line(num_test, test_list, rules):
    for i in test_list:
        for j in rules:
            if num_test == j[1] and i == j[0]:
                return (False, j)
    return (True, None)


def check_all_lines(list_of_lines):
    correct_pages = []
    wrong_pages = []
    for x in list_of_lines:
        status = True
        for i, v in enumerate(x):
            test_list = x[i:]
            status, target = check_single_line(v, test_list, rules)
            if not status:
                break
        if status:
            correct_pages.append((x))
        if not status:
            wrong_pages.append([x, target])
    return wrong_pages, correct_pages



def fix_mistakes(broken_line):
    mistake = broken_line[0]
    rule = broken_line[1]
    first_index = mistake.index(rule[0])
    second_index = mistake.index(rule[1])
    mistake[first_index] = rule[1]
    mistake[second_index] = rule[0]
    return mistake
    



def fix_wrong_lines(wrong_lines):
    corrected = []
    for i in wrong_lines:
        status = False
        line_to_fix = i.copy()
        while not status: 
            fixed_line = fix_mistakes(line_to_fix)
            for j, v in enumerate(fixed_line):
                test_list = fixed_line[j:]
                status, target = check_single_line(v, test_list, rules)
                if not status:
                    line_to_fix = (fixed_line, target)
                    break
            if status:
                print("Fixed line {}".format(i))
                corrected.append(fixed_line)
    return corrected

wrong_lines, correct_lines = check_all_lines(pages)
corrected_lines = fix_wrong_lines(wrong_lines)
values = [i[int(len(i)/2)] for i in corrected_lines]
print(sum(values))