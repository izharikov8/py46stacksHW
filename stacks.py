# stacks
check_list_balanced = ['(', '(', '(', '(', '(', '[', '{', '}', ']', ')', ')', ')', ')', ')']
check_list_unbalanced = ['{', '{', '{', '}']
bal_1 = '(((([{}]))))'
bal_2 = '[([])((([[[]]])))]{()}'
bal_3 = '{{[()]}}'
bal_4 = '({[]})'
unbal_1 = '}{}'
unbal_2 = '{{[(])]}}'
unbal_3 = '[[{())}]'


# function
def stack_balance_check(data):
    if len(data) % 2 == 0:
        num = len(data) // 2
        idx = -1
        for el in data[:num]:
            if el == '(' and data[idx] == ')' \
                or el == '[' and data[idx] == ']' \
                    or el == '{' and data[idx] == '}':
                idx -= 1
            else:
                return 'Unbalanced'
        return 'Balanced'
    else:
        return 'Unbalanced'


# Строки
print(stack_balance_check(bal_1))
print(stack_balance_check(bal_2))
print(stack_balance_check(bal_3))
print(stack_balance_check(unbal_1))
print(stack_balance_check(unbal_2))
print(stack_balance_check(unbal_3))
print(stack_balance_check(bal_4))
print()
# Списки
print(stack_balance_check(check_list_balanced))
print(stack_balance_check(check_list_unbalanced))