# Написать функцию возвращающую четные элементы последовательности Фибоначчи.
# Например, f(4) вернет 0,2,8,34
class GenFibonacci:

    def __init__(self, number=100):
        self.limit = number
        self.counter = 0
        self.num_minus_one = -1
        self.num_one = 1

    def __next__(self):
        if self.counter >= self.limit:
            raise StopIteration
        result = self.num_minus_one + self.num_one
        self.num_minus_one = result
        self.num_minus_one, self.num_one = self.num_one, self.num_minus_one
        self.counter += 1
        return result

    def __iter__(self):
        return GenFibonacci(self.limit)


def f(n):
    fibonacci = GenFibonacci()
    list_even_number = [i for i in fibonacci if i % 2 == 0]
    print(f'Четные элементы последовательности Фибоначчи: {list_even_number[:n]}')


f(10)  # вернет 0,2,8,34