class Jar:
    def __init__(self, capacity=12):
        if int(capacity) < 0 or type(capacity) != int:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Cannot deposit more than the capacity allows")
        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Cannot withdraw more cookies than available")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
