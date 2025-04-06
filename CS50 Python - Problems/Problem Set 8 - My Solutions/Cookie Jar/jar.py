class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, addCookie):
        if not isinstance(addCookie, int) or addCookie <= 0:
            raise ValueError
        if (self._cookies + addCookie) > self._capacity:
            raise ValueError
        self._cookies += addCookie

    def withdraw(self, subCookie):
        if not isinstance(subCookie, int) or subCookie <= 0:
            raise ValueError
        if (self._cookies - subCookie) < 0:
            raise ValueError("Nom nom nom")
        self._cookies -= subCookie

    @property
    def capacity(self):
        return self._capacity
        
    @property
    def size(self):
        return self._cookies