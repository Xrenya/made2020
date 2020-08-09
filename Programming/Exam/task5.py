import sys
from operator import itemgetter


class Order(object):
    def __init__(self, free_time):
        self.user_id = None
        self.event_happened = [False] * 4
        self.free_time = free_time * 60   # бесплатное время ожидания
        self.ordered_at = None            # время заказа (Unix time)
        self.car_arrive_time = None       # ожидаемое время подачи машины в минутах
        self.travel_time = None           # ожидаемая длительность поездки в минутах
        self.arrived_at = None            # время подачи машины (Unix time)
        self.started_at = None            # пользователь сел в машине и началась поездка (Unix time)
        self.finished_at = None           # поездка завершилась (Unix time)
        self.expected_arrival = None
        self.late_time = None
        self.is_guilty = None
        self.diff_time = None

    def add_event(self, log):
        event_name = log[0]
        if event_name == "ordered":
            self.ordered(*log[-4:])
        elif event_name == "arrived":
            self.arrived(log[-1])
        elif event_name == "started":
            self.started(log[-1])
        elif event_name == "finished":
            self.finished(log[-1])

    def ordered(self, user_id, ordered_at, car_arrive_time, travel_time):
        self.user_id = user_id
        self.ordered_at = int(ordered_at)
        self.car_arrive_time = int(car_arrive_time) * 60
        self.travel_time = int(travel_time) * 60
        self.event_happened[0] = True

    def arrived(self, arrived_at):
        self.arrived_at = int(arrived_at)
        self.event_happened[1] = True

    def started(self, started_at):
        self.started_at = int(started_at)
        self.event_happened[2] = True

    def finished(self, finished_at):
        self.finished_at = int(finished_at)
        self.event_happened[3] = True

    def eval_expected_arrival(self):
        # предполагаемого времени подачи машины X,
        # бесплатного времени ожидания K и
        # предполагаемой длительности поездки Y
        expected_arrival = self.ordered_at + self.car_arrive_time + self.free_time + self.travel_time
        return expected_arrival

    def eval_late(self):
        # время опоздания
        self.expected_arrival = self.eval_expected_arrival()
        self.late_time = self.finished_at - self.expected_arrival

    def eval_guilty(self):
        # если пользователь не садился в машину дольше K минут после подачи, мы считаем его виноватым в своем опоздании
        self.is_guilty = self.arrived_at + self.free_time < self.started_at

    def get_result(self):
        if not all(self.event_happened):
            return 0, None
        self.eval_late()
        self.eval_guilty()
        self.diff_time = max(0, self.late_time) if not self.is_guilty else 0
        return -self.diff_time, self.user_id


def main():
    num_iter = int(sys.stdin.readline())

    for n_iter in range(num_iter):
        orders = dict()
        n_events, n_users, free_waiting_time = map(int, sys.stdin.readline().split())
        for _ in range(n_events):
            event_log = sys.stdin.readline().split()

            order_id = event_log[1]
            if order_id not in orders:
                orders[order_id] = Order(free_waiting_time)
            orders[order_id].add_event(event_log)

        users = dict()
        for order in orders.values():
            neg_time, user_id = order.get_result()
            if neg_time < 0:
                if user_id not in users:
                    users[user_id] = 0
                users[user_id] += neg_time

        users = sorted(users.items(), key=lambda x: (x[1], x[0]))
        result = [user_id for user_id, neg_time in users[:n_users] if neg_time < 0]
        print(' '.join(result) if len(result) > 0 else '-')


if __name__ == '__main__':
    main()
