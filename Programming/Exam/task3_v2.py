import sys
from math import gcd


class Node(object):
    def __init__(self, val):
        self.val = int(val)
        self.sums = list()

    def append(self, top_node):
        for top_val in top_node.sums:
            self.sums.append(self.val + top_val)


def get_ans(leaves):
    all_sums = list()
    for node in leaves:
        all_sums += node.sums
    numerator = sum(all_sums)
    nominator = len(all_sums)
    nod = gcd(numerator, nominator)
    numerator = 0 if numerator == 0 else numerator // nod
    nominator = 1 if numerator == 0 else nominator // nod
    return numerator, nominator


def solve(tree):
    tree[0][0].sums.append(tree[0][0].val)
    for i in range(len(tree) - 1):
        top = tree[i]
        bottom = tree[i + 1]
        for j in range(len(top)):
            bottom[j].append(top[j])
            bottom[j + 1].append(top[j])
    return get_ans(tree[-1])


def main():
    num_iter = int(sys.stdin.readline())

    for n_iter in range(num_iter):
        tree = list()
        height = int(sys.stdin.readline())
        for level in range(height):
            cells = list(map(Node, sys.stdin.readline().split()))
            tree.append(cells)
        numerator, nominator = solve(tree)
        print(numerator, nominator)


if __name__ == '__main__':
    main()
