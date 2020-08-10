import sys
from collections import deque
from copy import deepcopy


def check_list(tag_list, stack=None):
    if stack is None:
        stack = deque()
    for i, tag in enumerate(tag_list):
        if tag.startswith('</'):
            try:
                last_tag = stack.pop()
            except IndexError:
                return stack, i, tag, None, 1
            if last_tag[1:-1] != tag[2:-1]:
                return stack, i, tag, last_tag, 1 + len(stack)
        else:
            stack.append(tag)
    return stack, None, None, None, len(stack)


def solve(tag_list):
    stack, idx_fail, tag_fail, prev_tag_fail, n_errors = check_list(tag_list, stack=None)
    if idx_fail is None:
        if n_errors == 0:
            return 'CORRECT'
        elif n_errors == 1:
            tag_fail = stack.pop()
            return f'ALMOST {tag_fail.upper()}'
        else:
            return 'INCORRECT'

    stack2, idx_fail2, tag_fail2, prev_tag_fail2, n_errors2 = check_list(tag_list[idx_fail:], stack=deepcopy(stack))
    if prev_tag_fail is not None:
        stack.append(prev_tag_fail)
        stack3, idx_fail3, tag_fail3, prev_tag_fail3, n_errors3 = check_list(tag_list[idx_fail + 1:], stack=deepcopy(stack))
    else:
        n_errors3 = 100
    if n_errors2 > 0 and n_errors3 > 0:
        return 'INCORRECT'
    if n_errors2 > 0:
        return f'ALMOST {tag_fail.upper()}'
    if n_errors3 > 0:
        return f'ALMOST {prev_tag_fail.upper()}'
    return f'ALMOST {tag_fail.upper()}'


def main():
    num_iter = int(sys.stdin.readline())

    for n_iter in range(num_iter):
        n_tags = int(sys.stdin.readline())
        tag_list = list()
        for _ in range(n_tags):
            tag = sys.stdin.readline().lower().strip()
            tag_list.append(tag)
        ans = solve(tag_list)
        print(ans)


if __name__ == '__main__':
    main()
