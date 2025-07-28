#Ітератори:
#Реалізуйте ітератор для зворотного виведення елементів списку.
import self


class ReverseList:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


# Приклад:
for item in ReverseList([1, 2, 3, 4, 'a', 2, 5, 7]):
    print(item)

#Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            if self.current % 2 == 0:
                result = self.current
                self.current += 1
                return result
            self.current += 1
        raise StopIteration

for num in EvenNumbers(10):
    print(num)

