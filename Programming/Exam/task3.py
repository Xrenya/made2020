import sys
from math import gcd


class Node(object):
    def __init__(self, val):
        self.val = int(val)
        self.sum = 0
        self.n_parents = 0

    @property
    def mean(self):
        if self.n_parents == 0:
            return self.val
        return self.sum / self.n_parents

    def append(self, top_node):
        self.sum += (self.val + top_node.mean) * top_node.n_parents
        self.n_parents += top_node.n_parents


def solve(tree):
    tree[0][0].sum = tree[0][0].val
    tree[0][0].n_parents = 1
    for i in range(len(tree) - 1):
        top = tree[i]
        bottom = tree[i + 1]
        for j in range(len(top)):
            bottom[j].append(top[j])
            bottom[j + 1].append(top[j])

    all_sums = [int(node.sum) for node in tree[-1]]
    all_nodes = [node.n_parents for node in tree[-1]]
    numerator = sum(all_sums)
    nominator = sum(all_nodes)
    nod = gcd(numerator, nominator)
    return numerator // nod, nominator // nod


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
