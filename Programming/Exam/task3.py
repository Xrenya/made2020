import sys


class Node(object):
    def __init__(self, val):
        self.val = int(val)
        self.sum = [self.val]

    def append(self, other_node):
        new_sum = list()
        for i in range(len(self.sum)):
            for j in range(len(other_node.sum)):
                curr_sum = (self.sum[i] + other_node.sum[j]) / len(self.sum)
                new_sum.append(curr_sum)
        self.sum = new_sum


def solve(tree):
    for i in range(len(tree) - 1):
        top = tree[i]
        bottom = tree[i + 1]
        for top_node in top:
            for bot_node in bottom:
                bot_node.append(top_node)

    all_sums = list()
    for node in tree[-1]:
        all_sums += node.sum
    numerator = sum(all_sums)
    nominator = len(all_sums)
    return numerator, nominator


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
