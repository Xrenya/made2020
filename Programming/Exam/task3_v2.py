import sys
from math import gcd
import numpy as np


class Node(object):
    def __init__(self, val):
        self.val = int(val)
        self.sums = np.array([], dtype=int)

    def append(self, top_node):
        self.sums = np.append(self.sums, top_node.sums + self.val)


def get_ans(leaves):
    # print(leaves)
    all_sums = np.concatenate([node.sums for node in leaves])
    numerator = sum(all_sums)
    nominator = len(all_sums)
    # print(all_sums)
    nod = gcd(numerator, nominator)
    numerator = 0 if numerator == 0 else numerator // nod
    nominator = 1 if numerator == 0 else nominator // nod
    return numerator, nominator


def solve(tree):
    tree[0][0].sums = np.array([tree[0][0].val], dtype=int)
    for i in range(len(tree) - 1):
        top = tree[i]
        bottom = tree[i + 1]
        for j in range(len(top)):
            bottom[j].add(top[j])
            bottom[j + 1].add(top[j])
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
