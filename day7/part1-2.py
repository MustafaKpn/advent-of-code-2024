import os

with open("input.txt", 'r') as f:
    read = f.readlines()


def evaluate(equation):
    cal = equation[0]
    for i in range(len(equation) - 1):
        if equation[i] == "*":
            cal *= equation[i+1]
        elif equation[i] == "+":
            cal += equation[i+1]
        elif equation[i] == "||":
            cal = int(str(cal) + str(equation[i+1]))
        
    return cal

def introduce_new_operator(equation_list, list_to_append):
    from itertools import combinations
    com = []
    indicies = [i for i in range(1, len(equation_list), 2)]

    for x in range(len(indicies) + 1):
        f = combinations(indicies, x)
        for i in f:
            if len(i) > 0:
                com.append(list(i))

    for i in com:
        y = equation_list.copy()
        for j in i:
            y[j] = "||"

        list_to_append.append(y)

    return list_to_append
        

def check_equation(line):
    import itertools
    
    x = ["+", "*"]
    result = int(line[:line.find(':')])
    numbers = line[line.find(":") + 1:].split()
    line_length = len(numbers) - 1
    combinations = list(itertools.product(x, repeat=line_length))
    all_equations = []
    new_all_equations = []
    for i in combinations:
        equation = []
        for j in range(len(numbers)-1):
            equation.append(int(numbers[j]))
            equation.append(i[j])
        equation.append(int(numbers[-1]))
        all_equations.append(equation)
    
    for i in all_equations:
        a = (introduce_new_operator(i, new_all_equations))
    
    all_equations += new_all_equations

    
    for m in all_equations:
        if evaluate(m) == result:

            return result
        

sum = 0
count = 0
for i in read:
    ex = check_equation(i.strip())
    count += 1
    if ex:
        sum += ex
        os.system('cls' if os.name == 'nt' else 'clear')
        print(count)
        

print(sum)

