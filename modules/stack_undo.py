def push(stack, item):
    stack.append(item)


def pop(stack):
    if stack:
        return stack.pop()
    return None


def peek(stack):
    if stack:
        return stack[-1]
    return None


def is_empty(stack):
    return len(stack) == 0