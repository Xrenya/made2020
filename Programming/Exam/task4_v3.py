import sys
from collections import deque
import re


def loop(tag_str, match):
    while match is not None:
        tag_str = tag_str[:match.start()] + tag_str[match.end():]
        match = re.search(r'<[a-zA-Z]+></[a-zA-Z]+>', tag_str)
    return tag_str


def solve(tag_str):
    match = re.search(r'<[a-zA-Z]+></[a-zA-Z]+>', tag_str)
    tag_str = loop(tag_str, match)
    # while match is not None:
    #     tag_str = tag_str[:match.start()] + tag_str[match.end():]
    #     match = re.search(r'<\w+></\w+>', tag_str)
    if len(tag_str) == 0:
        return 'CORRECT'
    elif tag_str.count('<') == 1:
        return f'ALMOST {tag_str.upper()}'
    else:
        match = re.search(r'<[a-zA-Z]+></?[a-zA-Z]+></[a-zA-Z]+>', tag_str)
        tag_str = loop(tag_str, match)
        if len(tag_str) == 0:
            ans = match.group(0).split('>')[1] + '>'
            return f'ALMOST {ans.upper()}'
        elif tag_str.count('<') == 1:
            return f'INCORRECT'


def main():
    num_iter = int(sys.stdin.readline())

    for n_iter in range(num_iter):
        n_tags = int(sys.stdin.readline())
        tag_str = ''
        for _ in range(n_tags):
            tag = sys.stdin.readline().lower().strip()
            tag_str += tag
        ans = solve(tag_str)
        print(ans)


if __name__ == '__main__':
    main()
