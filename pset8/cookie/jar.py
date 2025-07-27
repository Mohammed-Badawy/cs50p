class Jar:
    # Initialize jar 
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    # Return str to be printed
    def __str__(self):
        return "🍪" * self._size

    # Add cookies to jar
    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Exceed cookie's jar capacity")
        self._size += n

    # Withdraw cokkies from jar
    def withdraw(self, n):
        if n > self._size:
            raise ValueError("There aren't enough cookies")
        self._size -= n

    # Return jar capacity
    @property
    def capacity(self):
        return self._capacity

    # Put jar capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity <= 0:
            raise ValueError("Can't be negative number")
        self._capacity = capacity

    # Return number of cookies in jar
    @property
    def size(self):
        return self._size
    
    # Initialize number of cookies in a jar
    @size.setter
    def size(self, size):
        self._size = size
