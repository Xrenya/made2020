import sys
from collections import namedtuple, deque


def check_tag(tag, mystack, n_errors, error_tag):
    try:
        last_tag = mystack.pop()
    except IndexError:
        error_tag = tag
        n_errors += 1
        return mystack, n_errors, error_tag

    if last_tag.name != tag.name:
        n_errors += 1
        try:
            prelast_tag = mystack.pop()
        except IndexError:
            mystack.append(last_tag)
            error_tag = tag
            return mystack, n_errors, error_tag

        if prelast_tag.name == tag.name:
            error_tag = last_tag
        else:
            error_tag = tag
            mystack.append(prelast_tag)
            mystack.append(last_tag)
    return mystack, n_errors, error_tag


def main():
    num_iter = int(sys.stdin.readline())
    tag_class = namedtuple('tag', ['name', 'all'])

    for n_iter in range(num_iter):
        mystack = deque()
        n_errors = 0
        error_tag = None
        n_tags = int(sys.stdin.readline())
        for _ in range(n_tags):
            in_tag = sys.stdin.readline().lower().strip()
            if in_tag[:2] == '</':
                # CLOSE TAG
                tag = tag_class(in_tag[2:-1], in_tag)
                mystack, n_errors, error_tag = check_tag(tag, mystack, n_errors, error_tag)
            else:
                # OPEN TAG
                tag = tag_class(in_tag[1:-1], in_tag)
                mystack.append(tag)

        if n_errors > 1 or len(mystack) > 1:
            print("INCORRECT")
        elif len(mystack) == 1 and n_errors == 1:
            print("INCORRECT")
        elif len(mystack) == 1:
            error_tag = mystack.pop()
            print(f"ALMOST {error_tag.all.upper()}")
        elif n_errors == 1:
            print(f"ALMOST {error_tag.all.upper()}")
        else:
            print("CORRECT")


if __name__ == '__main__':
    main()
