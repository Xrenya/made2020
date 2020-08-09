import sys
import math


def eval_comb(n, k=2):
    if n < 2:
        return 0
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def solve(data):
    ans = 0
    all_x = list(data.keys())
    for i in range(len(all_x)):
        for j in range(i + 1, len(all_x)):
            n_comb = eval_comb(len(data[all_x[i]] & data[all_x[j]]))
            ans += n_comb
    return int(ans)


def main():
    num_iter = int(sys.stdin.readline())

    for n_iter in range(num_iter):
        data = dict()
        cross_num = int(sys.stdin.readline())
        for coord in range(cross_num):
            x, y = map(int, sys.stdin.readline().split())
            if x not in data:
                data[x] = set()
            data[x].add(y)
        n_rectangles = solve(data)
        print(n_rectangles)


if __name__ == '__main__':
    main()
