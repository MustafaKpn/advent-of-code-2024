



with open('input.txt', 'r') as f:
    lines = f.readlines()

def check1(report):
    sorted_lists = [sorted(report), sorted(report, reverse=True)]
    
    return report in sorted_lists



def check2(report):
    for i in range(1, len(report)):
        if (abs(int(report[i-1]) - int(report[i])) > 3) or ((abs(int(report[i-1]) - int(report[i]))) < 1) or (int(report[i-1]) == int(report[i])):
            return False
    return True

def dampener(report):
    state = False
    for i in range(len(report)):
        dampened_report = report.copy()
        dampened_report.pop(i)
        if check1(dampened_report) and check2(dampened_report):
            return True
    return False

safe_reports = 0
non = 0
for line in lines:
    line = line.strip().split(' ')
    line = [int(i) for i in line]
    if ((len(line) > 1) and check1(line) and check2(line)):
        safe_reports += 1
    elif dampener(line):
        non += 1
