"""
Условия

Если задача не отображается, то вы либо не авторизованы, либо не нажали кнопку кнопку «принять участие» на этой странице.

Для 1-го теста на мишени всегда назначен черный сектор.
Для 2-го теста на мишенях черный сектор может назначаться, а может и не назначаться.

Игра в Дартс 3000 проходит следующим образом.

На круглой мишени изначально N секторов. В начале игры для каждого сектора ведущий записывает баллы. Баллы сектора могут быть как положительными, так и отрицательными. Также, по своему усмотрению, ведущий может назначить один произвольный сектор специальным черным сектором (важно — ведущий может и не назначать черный сектор вообще).
Далее каждому игроку выдается ровно 2 дротика — красный и синий. В свой ход игрок бросает оба дротика в мишень. Результатом его броска считается сумма баллов на секторах, которые идут от красного сектора (сектор, в который игрок попал красным дротиком) до синего сектора (сектор, в который игрок попал синим дротиком) по часовой стрелке. Красный и синий сектор также включаются в эту сумму.

    Если игрок попал дротиками в один сектор, то его результат — это просто баллы на этом одном секторе, а не сумма на всей мишени.
    Если в этом промежутке от красного до синего сектора (включая красный и синий) встретился черный сектор, то тогда результат игрока считается равным 0.

Побеждает в раунде тот, кто после броска набрал максимальный результат.

Ваша задача — для данной мишени определить максимальный возможный результат, который может получить игрок.



Формат входных данных

Первая строка теста содержит одно целое число x — количество наборов входных данных. После следуют x наборов данных.
В первой строке набора записаны два числа, разделенные пробелом: N и K.

N — количество секторов на мишени. K — номер сектора, который был назначен черным. Сектора нумеруются с 0. Если K = -1, то это означает, что в этом раунде ведущий не назначил черный сектор.
Во второй строке набора записано N чисел, разделенных пробелом — баллы за сектора. Сектора указаны по часовой стрелке начиная с нулевого сектора. Важно отметить, что число K означает номер сектора именно в указанном порядке.
Формат выходных данных

Для каждого набора данных необходимо вывести одно число (каждое на отдельной строке) — максимальный результат, который может получить игрок.

"""
import sys


def solve(sectors, k=-1):
    ssum = 0
    ans = 0
    seq_len = 0
    for i in range(2 * len(sectors) - 1):
        if k > 0 and i % len(sectors) == k:
            ssum = 0
        else:
            ssum += sectors[i % len(sectors)]

        if seq_len == len(sectors):
            ssum -= sectors[i % len(sectors) - 1]
            seq_len = seq_len if ssum else 0
        else:
            seq_len = seq_len + 1 if ssum else 0

        ans = max(ans, ssum)
        ssum = max(ssum, 0)

    print(ans)
    return ans


def deb_py():
    with open(r'D:\SakaevRF\reps\made2020\Programming\testf.txt', 'r') as f:
        num_iter = f.readline()
        n, k = map(int, f.readline().split())
        sectors = tuple(map(int, f.readline().split()))
    ans = solve(sectors, k)


def main():
    # n_iter = int(input())
    # n, k = map(int, input().split())
    # sectors = list(map(int, input().split()))
    # reader = (map(int, line.split()) for line in sys.stdin)
    num_iter = int(sys.stdin.readline())

    for n_iter in range(num_iter):
        n, k = map(int, sys.stdin.readline().split())
        sectors = tuple(map(int, sys.stdin.readline().split()))

        ans = solve(sectors, k)
        print(ans)


if __name__ == '__main__':
    deb_py()

    # assert solve([2, 3, 4, 5, -30, 6, -1, 2], k=2) == 12
    # assert solve([1, -3, 2, -2, 3, 4]) == 8
    # assert solve([1, 2, 3]) == 6
    # assert solve([3, 2, 1]) == 6
    # assert solve([5, -10, 5]) == 10
    # assert solve([-10, 5, 5]) == 10
    # assert solve([5, 5, -10]) == 10
    # assert solve([-10, -10, 5]) == 5
    # assert solve([-10, 5, -10]) == 5
    # assert solve([5, -10, -10]) == 5
    # assert solve([5, -10, 5, -11]) == 5
    # assert solve([5, 5, -11, 5, 6, -11]) == 11

    # main()