from stack import Stack


def balanced(user_str):
    stack = Stack()
    balance = True
    index = 0
    while index < len(user_str) and balance:
        symbol = user_str[index]
        if symbol in "([{":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balance = False
            else:
                top = stack.pop()
                if not matches(top, symbol):
                    balance = False
        index += 1
    if balance and stack.is_empty():
        return "сбалансировано"
    else:
        return "не сбалансировано"


def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


if __name__ == '__main__':
    # сбалансированные
    string_1 = '(((([{}]))))'
    string_2 = '[([])((([[[]]])))]{()}'
    string_3 = '{{[()]}}'

    # несбалансированные
    string_4 = '}{}'
    string_5 = '{{[(])]}}'
    string_6 = '[[{())}]'

    print(balanced(string_1))
    print(balanced(string_2))
    print(balanced(string_3))
    print(balanced(string_4))
    print(balanced(string_5))
    print(balanced(string_6))
