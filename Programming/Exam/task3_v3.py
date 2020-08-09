import sys
from math import gcd


class Node(object):
    def __init__(self, val):
        self.val = int(val)
        self.sum = 0
        self.n_parents = 0

    def add(self, top_node):
        self.sum += self.val * top_node.n_parents + top_node.sum
        self.n_parents += top_node.n_parents


def get_ans(leaves):
    numerator = 0
    nominator = 0
    # суммируем все итоговые суммы
    for node in leaves:
        numerator += node.sum
        nominator += node.n_parents
    nod = gcd(numerator, nominator)
    numerator = 0 if numerator == 0 else numerator // nod
    nominator = 1 if numerator == 0 else nominator // nod
    return numerator, nominator


def solve(tree):
    tree[0][0].sum = tree[0][0].val
    tree[0][0].n_parents = 1

    # проходим по уровням
    for i in range(len(tree) - 1):
        top = tree[i]
        bottom = tree[i + 1]

        # прибавляем значения верхних узлов в нижние левые и правые листья
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
