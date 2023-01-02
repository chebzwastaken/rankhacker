class LinearProbe:
    def __init__(self, size):
        self.M = size

        self.a = [None] * size
        # d is for data
        self.d = [None] * size

    def hash(self, key):
        return key % self.M

    def put(self, key, data):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while True:
            if self.a[i] == None:
                self.a[i] = key
                self.d[i] = data
                return
            if self.a[i] == key:
                self.d[i] = data
                return
            j += 1
            i = (initial_position + j) % self.M
            if i == initial_position:
                break

    def get(self, key):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]
            j += 1
            i = (initial_position + j) % self.M
            if i == initial_position:
                return None
        return None

    def delete(self, key):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while self.a[i] != None:
            if self.a[i] == key:
                self.a[i] = None
                self.d[i] = None
                return
            j += 1
            i = (initial_position + j) % self.M
            if i == initial_position:
                return
        return

    def print_table(self):
        for i in range(self.M):
            print("[%02d] %s %s" % (i, self.a[i], self.d[i]))

if __name__ == "__main__":
    lp = LinearProbe(42)
    for i in range(100):
        lp.put(i, i)
    lp.print_table()
