import sys
from collections import deque
from copy import deepcopy


class HTML(object):
    def __init__(self):
        self.stack = deque()
        self.n_errors = 0
        self.error_tag = None

    def add(self, tag):
        # Возвращает True если нужно создать копию
        if '/' not in tag:  # если тег открывающий
            self.stack.append(tag)
        else:  # если тег закрывающий
            # достаем последний открывающий
            try:
                last_tag = self.stack.pop()
            except IndexError:
                # если стек пустой
                self.n_errors += 1
                self.error_tag = tag
                return False

            # если закрывающий тег не совпадает с открывающим:
            if last_tag[1:-1] != tag[2:-1]:
                self.error_tag = tag                # запоминаем тег,
                self.n_errors += 1                  # увеличиваем счетчик ошибок,
                self.stack.append(last_tag)         # возвращаем last_tag
                return True
        return False

    def get_errors(self):
        result_n_errors = self.n_errors + len(self.stack)
        if len(self.stack) == 1:
            self.error_tag = self.stack.pop()
        return result_n_errors

    def get_result(self):
        result_n_errors = self.get_errors()
        if result_n_errors > 1:
            print("INCORRECT")
        elif result_n_errors == 1:
            print(f"ALMOST {self.error_tag.upper()}")
        else:
            print("CORRECT")


def main():
    num_iter = int(sys.stdin.readline())

    for n_iter in range(num_iter):
        html = HTML()
        n_tags = int(sys.stdin.readline())
        for _ in range(n_tags):
            tag = sys.stdin.readline().lower().strip()
            html.add(tag)
        html.get_result()


if __name__ == '__main__':
    main()
