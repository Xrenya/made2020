import sys


def get_sum(num):
    if num not in sequence:
        sequence[num] = int(num * (num + 1) / 2)
    return sequence[num]


def solve(k):
    last_sum = 0
    i = 0
    while True:
        i += 1
        sum_n = get_sum(i)
        if last_sum < k <= sum_n:
            break
        last_sum = sum_n

    ans = ['1'] + ['0'] * i
    ans[last_sum - k] = '1'
    ans = int(''.join(ans), 2) % CONST
    return ans


def main():
    num_iter = int(sys.stdin.readline())

    for n_iter in range(num_iter):
        k = int(sys.stdin.readline())
        ans = solve(k)
        print(ans)


if __name__ == '__main__':
    CONST = 35184372089371
    sequence = dict()
    main()
