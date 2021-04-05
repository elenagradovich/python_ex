''' Итератор. Для этого нужно написать класс и реализовать методы __iter__() и __next__(). После этого требуется настроить внутренние состояния и вызывать исключение StopIteration, когда больше нечего возвращать.

class TribonacciGenerator:
    def __init__(self, limit):
        self.prev_prev = 0
        self.prev = 1
        self.cur = 1
        self.limit = limit
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.limit:
            result = self.prev_prev
            self.prev_prev, self.prev, self.cur = self.prev, self.cur, self.prev + self.cur + self.prev_prev
            self.i += 1
            return result
        else:
            raise StopIteration

for i in TribonacciGenerator(35):
    print(i)


'''


# Генератор - место return используется инструкция yield. Она уведомляет интерпретатор Python о том, что это генератор, и возвращает итератор.

def tribonacciGenerator(limit):
    prev_prev = 0
    prev = 1
    cur = 1
    count = 0

    while count < limit:
        result = prev_prev
        prev_prev, prev, cur = prev, cur, prev + cur + prev_prev
        count += 1
        yield result


for item in tribonacciGenerator(35):
    print(item)
