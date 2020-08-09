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
        # суммарное количество ошибок = n_errors + остатки стека
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
        html_copy = None
        n_tags = int(sys.stdin.readline())
        for _ in range(n_tags):
            tag = sys.stdin.readline().lower().strip()
            create_copy = html.add(tag)

            if create_copy and html_copy is None:
                # если нужна копия и ее нет - создаем и убираем последний элемент из стека
                html_copy = deepcopy(html)
                html_copy.error_tag = html_copy.stack.pop()
            if html_copy is not None:
                # если есть копия, добавляем в нее тег
                html_copy.add(tag)

                if html_copy.n_errors > 1:
                    # если много ошибок - можно дальше не считать
                    html_copy = None
                elif html.n_errors > html_copy.n_errors:
                    # если количество ошибок в копии меньше чем в орининале - производим замену
                    html, html_copy = html_copy, None

        if html_copy is not None and html.get_errors() > html_copy.get_errors():
            # если количество ошибок в копии меньше чем в орининале - производим замену
            html, html_copy = html_copy, None
        html.get_result()


if __name__ == '__main__':
    main()
