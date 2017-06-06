#!/usr/bin/env python3
opes_values = {'*': 2, '/': 2, '+': 1, '-': 1}
operators = ['*', '/', '+', '-']


def main(argv):
    formula_list = list(argv[0])
    while ' ' in formula_list:
        formula_list.remove(' ')
    buf = []
    stack = []
    if len(formula_list) == 0:
        return 1
    if formula_list.count('(') != formula_list.count(')'):
        return 3
    before_formula = "None"
    for f in formula_list:
        if not f.isdigit() and f not in operators and f != '(' and f != ')':
            return 2
        elif f.isdigit():
            if before_formula == "Digit":
                return 4
            else:
                buf.append(f)
                before_formula == "Digit"
        elif f == ')':
            if len(stack) > 0:
                while len(stack) > 0:
                    tmp = stack.pop()
                    if tmp == '(':
                        break
                    else:
                        buf.append(tmp)
            else:
                return
        elif f == '(':
            stack.append(f)
        else:
            if before_formula == "Ope":
                return 4
            while len(stack) > 0:
                if stack[len(stack) - 1] in operators and f in operators and \
                   opes_values[stack[len(stack) - 1]] > opes_values[f]:
                    tmp = stack.pop()
                    buf.append(tmp)
                else:
                    break
            stack.append(f)
            before_formula == "Ope"
    while len(stack) > 0:
        tmp = stack.pop()
        buf.append(tmp)
    formula = ' '.join(buf)

    stack = []
    for f in buf:
        if f.isdigit():
            stack.append(f)
        else:
            f1 = stack.pop()
            f2 = stack.pop()
            result = eval("{0} {1} {2}".format(f2, f, f1))
            stack.append(result)
    result = stack.pop()
    print("{0} = {1}".format(formula, result))
    return 0
